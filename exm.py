from jsproto import *
(var(['apple', 'banana', 'pear'])
 .forEach(function(lambda s: 'long' if len(s) > 5 else 'short')
          .then(print)))

(var({
    "name": "John",
    "age": 30,
    "contact": {
        "email": "john@example.com",
        "phone": "1234567890"
    },
    "hobbies": var(["reading", "swimming", "traveling"])
    .map(lambda s:s.upper())(),
    "is_student": False
}).contact.email
 .then(print))


my_dict = var({
    "name": "John",
    "age": 30,
    "contact": {
        "email": "john@example.com",
        "phone": "1234567890"
    },
    "hobbies": ["reading", "swimming", "traveling"],
    "is_student": False
})
my_dict.contact = var({})
print(my_dict.toString())
# 输出
# short
# long
# short
# john@example.com
# {}
