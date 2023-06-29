from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Auth,Customer1,Customer2
from django.contrib import messages



def loginpage(request):
    #create object for Auth table
    ob=Auth.objects.all().values()
    
    admin = ob[0]
    cust1 = ob[1]
    cust2= ob[2]
    
    #checking id and password are same
    if request.method == "POST":
        
        #getting the user input
        userid = request.POST["userid"]
        password = request.POST["password"]
        
        #for admin
        if(userid==admin['userid'] and password == admin['pasword']):
            #if id and password are correct redirect to adminpage
            return redirect('adminpage')
        
        #if admin id is correct but password is wrong
        elif(userid==admin['userid'] and password != admin['pasword']):
            messages.warning(request,"Invalid Admin Password")    
        
        #for customer1
        elif(userid==cust1['userid'] and password == cust1['pasword']):
            #if id and password are correct redirect to customer1 page
            return redirect('customer1')
        
        #if customer1 id is correct but password is wrong
        elif(userid==cust1['userid'] and password != cust1['pasword']):
            messages.warning(request,"Invalid Customer1 Password")

        #for customer2
        elif(userid==cust2['userid'] and password == cust2['pasword']):
            #if id and password are correct redirect to customer2
            return redirect('customer2')
        
        #if customer1 id is correct but password is wrong
        elif(userid==cust2['userid'] and password != cust2['pasword']):
            messages.warning(request,"Invalid Customer2 Password")
        
        #if userid and password doesn't match showerror
        else:
            messages.warning(request,"invalid entry")

    return render(request,"index.html",{})


def customer1(request):
    
    if request.method == "POST":
        #creating object for Customer1 table
        #getting input from the user in all the tables
        
        cust1values = Customer1(orderDate = request.POST['orderDate'],company =request.POST['company'] ,owner = request.POST['owner'] 
                                ,item = request.POST['item'],quantity =request.POST['quantity'] ,weight = request.POST['weight'],
                                shipment = request.POST['shipment'],trackingId= request.POST['trackingId'] ,
                                shipmentSize = request.POST['shipmentSize'],boxCount =request.POST['boxCount'],
                                specification = request.POST['specification'],checklistQuantity =request.POST['checklistQuantity'])
        #save the details to database
        cust1values.save()
        return HttpResponseRedirect('/customer1?submitted=True')
    else:
        if 'submitted' in request.GET:
            #showing message that data has stored
            messages.info(request,"Your Data has been submitted successfully ")
            
    return render(request,"form.html",{})


def customer2(request):
    
    if request.method == "POST":
        #creating object for Customer2 table
        
        #getting input from the user in all the tables
        cust2values = Customer2(orderDate = request.POST['orderDate'],company =request.POST['company'] ,owner = request.POST['owner'] 
                                ,item = request.POST['item'],quantity =request.POST['quantity'] ,weight = request.POST['weight'],
                                shipment = request.POST['shipment'],trackingId= request.POST['trackingId'] ,
                                shipmentSize = request.POST['shipmentSize'],boxCount =request.POST['boxCount'],
                                specification = request.POST['specification'],checklistQuantity =request.POST['checklistQuantity'])
        #save the details to database
        cust2values.save()
        
        return HttpResponseRedirect('/customer2?submitted=True')
    else:
        if 'submitted' in request.GET:
            #showing message that data has stored
            messages.info(request,"Your Data has been submitted successfully ")
            
    return render(request,"form.html",{})


def adminpage(request):
    
    #creating objects for customer1 and customer2 tables
    
    #selecting quantity from the table
    quantity1List = Customer1.objects.values_list("quantity",flat=True)
    quantity2List = Customer2.objects.values_list("quantity",flat=True)
    
    #selecting weight from the table
    weight1List = Customer1.objects.values_list("weight",flat=True)
    weight2List = Customer2.objects.values_list("weight",flat=True)
    
    #selecting Box COunt from the table
    box1List = Customer1.objects.values_list("boxCount",flat=True)
    box2List = Customer2.objects.values_list("boxCount",flat=True)
    
    #summation of quantity    
    sumQ1=sum(quantity1List)   
    sumQ2=sum(quantity2List)
    
    #total customer1 and customer2 quatity
    totalQ = sumQ1+sumQ2
      
    #summation of weight
    sumW1=sum(weight1List)
    sumW2=sum(weight2List)
    
    #total customer1 and customer2 weight
    totalW = sumW1 + sumW2   
    #summation of boxcount
    sumB1=sum(box1List)
    sumB2=sum(box2List)
    
    #total customer1 and customer2 box count
    totalB = sumB1 + sumB2
        
    return render(request,"admin.html",{
        'sumQ1':sumQ1,
        'sumQ2':sumQ2,
        'totalQ':totalQ,
        'sumW1':round(sumW1,3),
        'sumW2':round(sumW2,3),
        'totalW':round(totalW,3),
        'sumB1':sumB1,
        'sumB2':sumB2,
        'totalB':totalB,       
        })