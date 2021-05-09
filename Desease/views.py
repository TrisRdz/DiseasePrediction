from django.shortcuts import render, redirect
from .models import user_registration
from .forms import user_cr
from .models import reg
from .models import feedback
# from django.core.context_processors import csrf
from .forms import reg1
from .forms import fb

# Create your views here.
pa = ''


def loging(request):
    username = request.POST['username']
    password = request.POST['password']
    user = user_registration.objects.filter(Username=username)
    pa = user.filter(Password=password)
    if user.filter(Password=password):
        na = user.only('Lname')
        return render(request, 'find.html')
    elif username == 'admin' and password == 'admin':
        user1 = user_registration.objects.all()
        return render(request, 'admin.html', {'user': user1})
    else:
        return render(request, 'loging.html')


def index(request):
    return render(request, 'index.html')


def log(request):
    return render(request, 'loging.html')


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def find(request):
    return render(request, "find.html")


def Hospitals(request):
    return render(request, "hospital.html")


def ff(request):
    return render(request, 'kk.html')


def sgn4(request):
    user = reg.objects.all()
    return render(request, 'add.html', {'user01': user})


def sgn3(request):
    user1 = user_registration.objects.all()
    return render(request, 'display.html', {'user0': user1})


def sgn0(request):
    return render(request, 'index.html')


def sgn2(request):
    if request.method == 'POST':
        form = reg1(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user1 = user_registration.objects.all()

            return render(request, 'admin.html')

    else:
        form = reg1()

    return render(request, 'create_user1.html', {
        'form': form,

    })


def usrcr(request):
    if request.method == 'POST':
        form = user_cr(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user1 = user_registration.objects.all()
            return render(request, 'base_admin.html', {'user': user1})

    else:
        form = user_cr()

    return render(request, 'create_user.html', {
        'form': form,

    })


def sgn(request):
    if request.method == 'POST':
        form = user_cr(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user1 = user_registration.objects.all()

            return render(request, 'loging.html')

    else:
        form = user_cr()

    return render(request, 'create_user.html', {
        'form': form,

    })


def delete_user(request):
    if request.method == 'POST':
        Delete = request.POST.get('name')
        user_registration.objects.filter(Username=Delete).delete()
        user1 = user_registration.objects.all()
        return render(request, 'admin.html', {'user': user1})


from django.contrib.auth import login, authenticate


def sel(request, sklearn=None):
    if request.method == 'POST':

        import numpy as np
        import pandas as pd
        # from gui_stuff import *
        gp1 = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
               'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
               ' Migraine', 'Cervical spondylosis']
        gp2 = ['Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid',
               'hepatitis A',
               'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
               'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)', ]
        gp3 = ['Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
               'Osteoarthristis',
               'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection',
               'Psoriasis',
               'Impetigo']

        l1 = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
              'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
              'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
              'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
              'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
              'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
              'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
              'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
              'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
              'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
              'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
              'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
              'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
              'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria',
              'family_history', 'mucoid_sputum',
              'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
              'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
              'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
              'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
              'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
              'yellow_crust_ooze']

        disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
                   'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
                   ' Migraine', 'Cervical spondylosis',
                   'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid',
                   'hepatitis A',
                   'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
                   'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
                   'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
                   'Osteoarthristis',
                   'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection',
                   'Psoriasis',
                   'Impetigo']

        l2 = []
        for x in range(0, len(l1)):
            l2.append(0)

        # TESTING DATA df -------------------------------------------------------------------------------------
        df = pd.read_csv("./Desease/static/images/Training.csv",engine='python',encoding = "utf-8-sig")

        df.replace(
            {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                           'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                           'Bronchial Asthma': 9, 'Hypertension ': 10,
                           'Migraine': 11, 'Cervical spondylosis': 12,
                           'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                           'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                           'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                           'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                           'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                           'Varicose veins': 30, 'Hypothyroidism': 31,
                           'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                           '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                           'Psoriasis': 39,
                           'Impetigo': 40}}, inplace=True)

        print(df.head())

        X = df[l1]

        y = df[["prognosis"]]
        np.ravel(y)
        # print(y)

        # TRAINING DATA tr --------------------------------------------------------------------------------
        tr = pd.read_csv("./Desease/static/images/Training.csv",engine='python', encoding = "utf-8-sig")
        tr.replace(
            {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                           'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                           'Bronchial Asthma': 9, 'Hypertension ': 10,
                           'Migraine': 11, 'Cervical spondylosis': 12,
                           'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                           'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                           'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                           'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                           'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                           'Varicose veins': 30, 'Hypothyroidism': 31,
                           'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                           '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                           'Psoriasis': 39,
                           'Impetigo': 40}}, inplace=True)

        X_test = tr[l1]
        y_test = tr[["prognosis"]]
        np.ravel(y_test)

        # ------------------------------------------------------------------------------------------------------
	
	

        # calculating accuracy-------------------------------------------------------------------
        from sklearn.naive_bayes import GaussianNB
        gnb = GaussianNB()
        gnb=gnb.fit(X,np.ravel(y))
        from sklearn.metrics import accuracy_score
        y_pred=gnb.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred, normalize=False))
        # -----------------------------------------------------
        # -----------------------------------------------------
        syp1 = request.POST.get('syp1')
        syp2 = request.POST.get('syp2')
        syp3 = request.POST.get('syp3')
        syp4 = request.POST.get('syp4')
        syp5 = request.POST.get('syp5')
        psymptoms = [syp1, syp2, syp3, syp4, syp5]
        for k in range(0, len(l1)):
            # print (k,)
            for z in psymptoms:
                if (z == l1[k]):
                    l2[k] = 1

        inputtest = [l2]
        predict = gnb.predict(inputtest)
        predicted = predict[0]

        h = 'no'
        for a in range(0, len(disease)):
            if (predicted == a):
                h = 'yes'
                break

        global dis
        dis = disease[a]
        print("==================================", dis)
        if dis in gp1:
            print("it is in gp1")
            # return render(request,'myapp/kk.html')
        elif dis in gp2:
            print("in gp2")
            # return render(request,'myapp/s.html')
        elif dis in gp3:
            print("in gp3")
            # return render(request,'myapp/h.html')

        return render(request, 'find.html', {'ss': disease[a]})
    else:
        return render(request, 'home.html')











