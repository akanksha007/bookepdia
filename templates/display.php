<html>
<h3>Images of books</h3>
<img src="/media/images/book_183225.jpg" />
<?php
{% for $p in photos %}
    $link_array = explode('/',$p);
    $page = end($link_array);
    
    <img src="<?php echo htmlspecialchars($page); ?>"  />
    
{% endfor %}
?>
</html>

<html>
<head>
    <title>{% if request.user.is_authenticated %}Logged In{% else %}Not Logged In{% endif %}</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css" />
</head>
<body class="{% if request.user.is_authenticated %}logged-in{% else %}logged-out{% endif %}">
 
{% if request.user.is_authenticated %}
    <a href="/accounts/logout/" class="pull-right">Logout</a>
    {% if request.user.first_name or request.user.last_name %}
        {{ request.user.first_name }} {{ request.user.last_name }}
    {% else %}
        {{ request.user.username }}
    {% endif %}
    {% if request.user.profile.account_verified %} (verified) {% else %} (unverified) {% endif %}
 
{% else %}
    <a href="/accounts/login/" class="pull-right">Login</a>
{% endif %}
</body>
</html>
