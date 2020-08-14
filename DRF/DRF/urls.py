
from django.urls import path, include




urlpatterns = [
    path('', include('snippets.urls')),
  
]

"""
Because we're using viewsets instead of views, 
we can automatically generate the URL conf for our API, 
by simply registering the viewsets with a router class.

Again, if we need more control over the API URLs we can 
simply drop down to using regular class-based views, and 
writing the URL conf explicitly.

Finally, we're including default login and logout views 
for use with the browsable API. That's optional, but useful 
if your API requires authentication and you want to use the browsable API.

"""
