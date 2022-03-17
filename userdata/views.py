from django.shortcuts import render

# Create your views here.
def formdata(request):
    """
    This definition handles both get and post.
    It serves the form for get , and for post 
    it takes the user data and puts it into 
    the database.
    """
    if request.method == 'GET':
        return render(request,'userdata/form.html')
    elif request.method == 'POST':
        # Add your logic to save the user data.
        # First get data from user using request.POST which returns a frozen dictionary.
        # Then put that data in a model that you have created.
        # Use modelName.objects.create(field1=value1,field2=value2,...) and store it 
        # in a variable , say mymodel 
        # Refer to userdata.models before doing so.
        
        
        # -----------------------------
        # Handling file save would be a bit more tricky.
        # The file doesn't go inside the post data. instead it goes
        # along with the post data and is accessible by using request.FILES
        # get the files from there and then store the files using:
        # file_obj = request.FILES.get('file_name')
        # Check if file is None or not. If not None 
        # let's assume , in mymodel , myfile is a fileField,
        # so to store the file in the mymodel ,, we would use the syntax :
        # mymodel.myfile.save(file_obj.name,file_obj)
        # This will in turn save your file in the media folder and store the 
        # link and  path to the file in the database.
        
        
        # then return thankyou.html.
        # Pass in whether it was successful in saving their data. 
        # If there was an error pass a context with variables to display the error.
        ...
        