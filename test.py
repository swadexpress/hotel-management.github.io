
import requests


while True:
    card_number  = int(input('enter card number :)'))
    payload = {'card_number': card_number}
    print (payload)
    r = requests.post("http://192.168.1.110:8000/shop/CardChackView/", data=payload)
    data  = r.json()
    # print(data['data'],'...............')
    data = data['data']
    for i in data:
        print ('Your Card Number : ',i["cardNumber"])
        print ('Your Status : ',i["status"])
        print ('Your bill Details : ',i["bills"])
    
    print('Your card number : ',card_number)



# class CardChackView(APIView):
#     def post(self, request, *args, **kwargs):
#         card_number = request.data.get('card_number', None)
#         data = CardChack.objects.filter(cardNumber=int(card_number))

#         data = list(data.values())
#         print (data)

#         responseData = {
#             'status': 'success', 
#             'data': data,

#             }

#         return JsonResponse(responseData, safe=False, status=HTTP_200_OK)




# class CardChack(models.Model):
#     STATUS = (
#         ('True', 'True'),
#         ('False', 'False'),
#     )    
#     BILLS_STATUS = (
#         ('BillPay', 'Bill Pay'),
#         ('YourBillDue', 'Your Bill Due'),
#     )
#     cardNumber  = models.CharField(max_length=50, blank=True, null=True)
#     status = models.CharField(max_length=10, choices=STATUS)
#     bills = models.CharField(max_length=15, choices=BILLS_STATUS)






