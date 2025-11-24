from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
# Create your views here.
from Remote_User.models import ClientRegister_Model,fraud_detection,detection_ratio,detection_accuracy

def login(request):


    if request.method == "POST" and 'submit1' in request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            enter = ClientRegister_Model.objects.get(username=username,password=password)
            request.session["userid"] = enter.id

            return redirect('ViewYourProfile')
        except:
            pass

    return render(request,'RUser/login.html')

def index(request):
    return render(request, 'RUser/index.html')

def Add_DataSet_Details(request):

    return render(request, 'RUser/Add_DataSet_Details.html', {"excel_data": ''})


def Register1(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        ClientRegister_Model.objects.create(username=username, email=email, password=password, phoneno=phoneno,
                                            country=country, state=state, city=city,address=address,gender=gender)

        obj = "Registered Successfully"
        return render(request, 'RUser/Register1.html',{'object':obj})
    else:
        return render(request,'RUser/Register1.html')

def ViewYourProfile(request):
    userid = request.session['userid']
    obj = ClientRegister_Model.objects.get(id= userid)
    return render(request,'RUser/ViewYourProfile.html',{'object':obj})


def Predict_Fraud_Detection_Type(request):
    if request.method == "POST":

        if request.method == "POST":

            Order_ID= request.POST.get('Order_ID')
            PDate= request.POST.get('PDate')
            Status= request.POST.get('Status')
            Fulfilment= request.POST.get('Fulfilment')
            Sales_Channel= request.POST.get('Sales_Channel')
            ship_service_level= request.POST.get('ship_service_level')
            Style= request.POST.get('Style')
            SKU= request.POST.get('SKU')
            Category= request.POST.get('Category')
            PSize= request.POST.get('PSize')
            ASIN= request.POST.get('ASIN')
            Qty= request.POST.get('Qty')
            currency= request.POST.get('currency')
            Amount= request.POST.get('Amount')
            payment_by= request.POST.get('payment_by')
            ship_city= request.POST.get('ship_city')
            ship_state= request.POST.get('ship_state')
            ship_postal_code= request.POST.get('ship_postal_code')
            ship_country= request.POST.get('ship_country')


        df = pd.read_csv('Datasets.csv')

        def apply_response(Label):
            if (Label == 0):
                return 0  # No Fraud Found
            elif (Label == 1):
                return 1  # Fraud Found

        df['Label'] = df['Label'].apply(apply_response)

        cv = CountVectorizer()
        X = df['Order_ID']
        y = df['Label']

        print("Order_ID")
        print(X)
        print("Results")
        print(y)

        cv = CountVectorizer()
        X = cv.fit_transform(X)

        models = []
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
        X_train.shape, X_test.shape, y_train.shape

        print("Naive Bayes")

        from sklearn.naive_bayes import MultinomialNB

        NB = MultinomialNB()
        NB.fit(X_train, y_train)
        predict_nb = NB.predict(X_test)
        naivebayes = accuracy_score(y_test, predict_nb) * 100
        print("ACCURACY")
        print(naivebayes)
        print("CLASSIFICATION REPORT")
        print(classification_report(y_test, predict_nb))
        print("CONFUSION MATRIX")
        print(confusion_matrix(y_test, predict_nb))
        models.append(('naive_bayes', NB))

        # SVM Model
        print("SVM")
        from sklearn import svm

        lin_clf = svm.LinearSVC()
        lin_clf.fit(X_train, y_train)
        predict_svm = lin_clf.predict(X_test)
        svm_acc = accuracy_score(y_test, predict_svm) * 100
        print("ACCURACY")
        print(svm_acc)
        print("CLASSIFICATION REPORT")
        print(classification_report(y_test, predict_svm))
        print("CONFUSION MATRIX")
        print(confusion_matrix(y_test, predict_svm))
        models.append(('svm', lin_clf))

        print("Logistic Regression")

        from sklearn.linear_model import LogisticRegression

        reg = LogisticRegression(random_state=0, solver='lbfgs').fit(X_train, y_train)
        y_pred = reg.predict(X_test)
        print("ACCURACY")
        print(accuracy_score(y_test, y_pred) * 100)
        print("CLASSIFICATION REPORT")
        print(classification_report(y_test, y_pred))
        print("CONFUSION MATRIX")
        print(confusion_matrix(y_test, y_pred))
        models.append(('logistic', reg))

        print("Decision Tree Classifier")
        dtc = DecisionTreeClassifier()
        dtc.fit(X_train, y_train)
        dtcpredict = dtc.predict(X_test)
        print("ACCURACY")
        print(accuracy_score(y_test, dtcpredict) * 100)
        print("CLASSIFICATION REPORT")
        print(classification_report(y_test, dtcpredict))
        print("CONFUSION MATRIX")
        print(confusion_matrix(y_test, dtcpredict))
        models.append(('DecisionTreeClassifier', dtc))

        classifier = VotingClassifier(models)
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)

        Order_ID1 = [Order_ID]
        vector1 = cv.transform(Order_ID1).toarray()
        predict_text = classifier.predict(vector1)

        pred = str(predict_text).replace("[", "")
        pred1 = pred.replace("]", "")

        prediction = int(pred1)

        if (prediction == 0):
            val = 'No Fraud Found in ECommerce Transaction'
        elif (prediction == 1):
            val = 'Fraud Found in ECommerce Transaction'


        print(val)
        print(pred1)

        fraud_detection.objects.create(Order_ID=Order_ID,
        PDate=PDate,
        Status=Status,
        Fulfilment=Fulfilment,
        Sales_Channel=Sales_Channel,
        ship_service_level=ship_service_level,
        Style=Style,
        SKU=SKU,
        Category=Category,
        PSize=PSize,
        ASIN=ASIN,
        Qty=Qty,
        currency=currency,
        Amount=Amount,
        payment_by=payment_by,
        ship_city=ship_city,
        ship_state=ship_state,
        ship_postal_code=ship_postal_code,
        ship_country=ship_country,
        Prediction=val)

        return render(request, 'RUser/Predict_Fraud_Detection_Type.html',{'objs': val})
    return render(request, 'RUser/Predict_Fraud_Detection_Type.html')



