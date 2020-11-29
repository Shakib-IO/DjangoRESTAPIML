#Throttling is similar to permissions, 
#in that it determines if a request should be authorized. 
# Throttles indicate a temporary state, and are used to control the rate of requests 
# that clients can make to an API.

#The UserRateThrottle will throttle users to a given rate of requests across the API. 
#The user id is used to generate a unique key to throttle against. 
#Unauthenticated requests will fall back to using the IP address 
#of the incoming request to generate a unique key to throttle against


from rest_framework.throttling import UserRateThrottle

#Custom Throttle classes

class LimitedRateThrottle(UserRateThrottle):
    scope = 'limited'

class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'