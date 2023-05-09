import os
import json
import facebook
access_token='EAADnd1v7RCEBAGQiAcBeXTiDgZAEWTYwm3MqlHGpMYkqiB7e7igIhbsnrVeLIdyrhmIoUZAZCtZA0fHqz4Uvj7HVELIDNnPDDly2uQEUVdgWatdR7Mcp92o21BoOKpbUZCnyRs93tUqYyI4M3xQ66ZCV1lE2hkqk1tqD1CwDsQ9WT6aQrRjeFt'
graph=facebook.GraphAPI(access_token)
print("Enter Your Post : ")
message=input("- ")
graph.put_object(parent_object='me', connection_name='feed', message=message)

