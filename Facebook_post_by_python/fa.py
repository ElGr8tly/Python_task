import os
import json
import facebook
access_token='EAALYgtNywfYBABHYHLbpKO2uFALZAq81ZACdisjyw2FKyciqUlEXlZAnh2VFUetPpZCIkIXutpWxThLB6k0Efcr6XLegO9SVLZBCZCY0BlC7AoDkEo1qvEq38AaeOVnbte0t6UR5TWnrQ6zkPU2QXMxqmYvJhuUYuAzAEeI4OdjW9BdCEHbGyec2cc0nRORRpi9QWXqRhMkjaXyIyGQTQ4'
graph=facebook.GraphAPI(access_token)
print("Enter Your Post : ")
message=input()
graph.put_object(parent_object='me', connection_name='feed', message=message)

