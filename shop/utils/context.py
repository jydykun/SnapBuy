APP_NAME = "SnapBuy"

def context_home():
    context = {
        "title" : f"Home | {APP_NAME}",
        "links" : [{
            "text" : "Men's Fashion",
            "url" : "shop:index",
            "image": "images/mens-fashion-link.jpg"
            },{
            "text" : "Womens's Fashion",
            "url" : "shop:index",
            "image": "images/womens-fashion-link.jpg"
            },{
            "text" : "Babies Fashion",
            "url" : "shop:index",
            "image": "images/babies-fashion-link.jpg"
            }],

        "tabs": [{
            "category" : "Men",
            "data" : "one",
            "products" : [{
                    "name": "Varsity Bomber Jacket",
                    "price" : "$28.99",
                    "image" : "shop/images/men-tshirt-three.webp"
                },{
                    "name": "Short Sleeve Pocket Tee",
                    "price" : "$5.98",
                    "image" : "shop/images/men-tshirt-one.webp"
                },{
                    "name": "Polo Shirt",
                    "price" : "$14.00",
                    "image" : "shop/images/men-tshirt-two.webp"
                },{
                    "name": "Warm Winter Coat",
                    "price" : "$64.99",
                    "image" : "shop/images/men-tshirt-four.webp"
                },{
                    "name": "5-Pack Crewneck Tee",
                    "price" : "$14.98",
                    "image" : "shop/images/men-tshirt-five.webp"
                },{
                    "name": "Beanies",
                    "price" : "$7.98",
                    "image" : "shop/images/men-tshirt-six.webp"
                }]
            },{
                "category" : "Women",
                "data" : "two",
                "products" : [{
                    "name": "Sweatshirt Crewneck",
                    "price" : "$12.00",
                    "image" : "shop/images/women-tshirt-one.webp"
                },{
                    "name": "Long Sleeve Crewneck",
                    "price" : "$12.99",
                    "image" : "shop/images/women-tshirt-two.webp"
                },{
                    "name": "Sweaters",
                    "price" : "$35.99",
                    "image" : "shop/images/women-tshirt-three.webp"
                },{
                    "name": "Fleece Joggers",
                    "price" : "$15.00",
                    "image" : "shop/images/women-tshirt-four.webp"
                },{
                    "name": "Zip-up Bodysuit",
                    "price" : "$18.98",
                    "image" : "shop/images/women-tshirt-five.webp"
                }]
            },{
                "category" : "Babies",
                "data" : "three",
                "products" : [{
                    "name": "Summer Clothes Set",
                    "price" : "$10.00",
                    "image" : "shop/images/babies-two.webp"
                },{
                    "name": "Baby Shirt Set",
                    "price" : "$10.39",
                    "image" : "shop/images/babies-one.webp"
                },{
                    "name": "Fleece Sweatpants",
                    "price" : "$3.00",
                    "image" : "shop/images/babies-three.webp"
                },{
                    "name": "Crew Kids Socks",
                    "price" : "$9.98",
                    "image" : "shop/images/babies-four.webp"
                },{
                    "name": "Hoodies Puffer Jacker",
                    "price" : "$14.98",
                    "image" : "shop/images/babies-five.webp"
                }]
            },{
                "category" : "Babies",
                "data" : "four",
                "products" : [{
                    "name": "Cozy Holiday Set",
                    "price" : "$11.98",
                    "image" : "shop/images/fashion-one.webp"
                },{
                    "name": "Summer Clothes Set",
                    "price" : "$10.00",
                    "image" : "shop/images/babies-two.webp"
                }]
            }],
        "testimonials": [{
                "name" : "John Doe",
                "role" : "Developer",
                "image": "shop/images/mens-fashion-link.jpg",
                "comment" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
                            Fusce pellentesque nibh neque, at volutpat dui congue ornare.\
                            Ut dignissim velit a lobortis scelerisque. Suspendisse potenti."
            },{
                "name" : "Jane Doe",
                "role" : "Designer",
                "image": "shop/images/womens-fashion-link.jpg",
                "comment" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
                            Fusce pellentesque nibh neque, at volutpat dui congue ornare.\
                            Ut dignissim velit a lobortis scelerisque. Suspendisse potenti."
            }],
        "yml" : [{
                "name": "Short Sleeve Pocket Tee",
                "price" : "$5.98",
                "discount" : "16.00",
                "image" : "shop/images/men-tshirt-one.webp"
            },{
                "name": "Polo Shirt",
                "price" : "$14.00",
                "discount" : "16.00",
                "image" : "shop/images/men-tshirt-two.webp"
            },{
                "name": "Sweatshirt Crewneck",
                "price" : "$12.00",
                "discount" : "69.99",
                "image" : "shop/images/women-tshirt-one.webp"
            },{
                "name": "Baby Shirt Set",
                "price" : "$10.39",
                "discount" : "12.99",
                "image" : "shop/images/babies-one.webp"
            }],
         "news" : [{
                "title": "Lorem ipsum dolor sit amet.",
                "content" : "Consectetur adipiscing elit. Fusce pellentesque nibh neque, at volutpat dui congue ornare.",
                "image" : "shop/images/mens-fashion-link.jpg"
            },{
                "title": "Lorem ipsum dolor sit amet.",
                "content" : "Consectetur adipiscing elit. Fusce pellentesque nibh neque, at volutpat dui congue ornare.",
                "image" : "shop/images/womens-fashion-link.jpg"
            },{
                "title": "Lorem ipsum dolor sit amet.",
                "content" : "Consectetur adipiscing elit. Fusce pellentesque nibh neque, at volutpat dui congue ornare.",
                "image" : "shop/images/babies-fashion-link.jpg"
            }]
        
    }
    return context
