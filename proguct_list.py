<!DOCTYPE html>
<html>
<head>
    <title>Магазин</title>
</head>
<body>
    <h1>Товари</h1>
    <ul>
        {% for product in products %}
            <li>
                <a href="{% url 'shop:product_detail' product.pk %}">{{ product.name }}</a> - {{ product.price }} грн
            </li>
        {% endfor %}
    </ul>
</body>
</html>
