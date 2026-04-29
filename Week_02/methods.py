"""
Using Methods WE declare a class name Phone and convert it into a object name my_name
"""
class phone:
    price = 120000
    brand = 'samsung'
    freature=['camera', 'light weight', 'orginal battery']

    def call(self):
        print("Hi I am calling")

    def send_sms(self, phone, mgs):
        text = f'The number is{phone} and the sms is {mgs}'
        return text
    
my_phone = phone()
print(my_phone.freature)
my_phone.call()
result = my_phone.send_sms(1993899080, 'Thank You')
print(result)

"""
Output:
['camera', 'light weight', 'orginal battery']
Hi I am calling
The number is1993899080 and the sms is Thank You
"""