<h3>Images of books</h3>
<img src="/media/images/book_183225.jpg" />

{% for p in photos %}
    
    
    <img src="{{p.photo.name}}" />
    
     
    
    
    {% endfor %}


