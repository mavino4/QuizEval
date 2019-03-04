from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from .models import *
import json 

# Create your views here.
def index(request):
	if request.method == 'GET':
		#leyendo la par'ametros enviados
	    data = {"quiz_id" : int(request.GET["quiz_id"]),
	    "pwd":request.GET["pwd"],
	    "answers" : request.GET["answers"]}

	    #validando la clave
	    ki = keys.objects.all().filter(key_i = data["pwd"])
	    #extrayendo las respuestas segun el id
	    Qi = Quiz.objects.all().filter(id= data["quiz_id"])
	    if bool(Qi):
	    	print(Qi[0].good_answer)
	    	print(data["answers"])

	    #evaluando resultado 
	    enviado = data["answers"].replace("[","").replace("]","").split(",")
	    correcto = Qi[0].good_answer.replace("[","").replace("]","").split(",")
	    resultadoEval = 0
	    if len(enviado) == len(correcto) and bool(Qi) and bool(ki):
	    	for i, j in zip(enviado, correcto):
	    		if int(i) == int(j) :
	    			resultadoEval += 1
	    	resultadoEval = ((resultadoEval / len(enviado))*100) //1
	    	#guardando submit
	    	sub_i = submition()
	    	sub_i.quizID =  ki[0].quizID
	    	sub_i.estID =  ki[0].estID
	    	sub_i.submit_date = timezone.now()
	    	sub_i.result = resultadoEval
	    	sub_i.save()
	    	msg = "Tu quiz se ha registrado existosamente"

	    else:
	    	print("Los resultados no coinciden")
	    	msg = "No se logro subir la prueba"
	    
	    
	    print("Resultado del submit", resultadoEval)
	
	return JsonResponse({"msg": msg, "nota": resultadoEval})

def quiz_id(request, q_id, asdf):
	return JsonResponse({"quiz_id": q_id, "text": text})
