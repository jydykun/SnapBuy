APP_NAME = "SnapBuy"

def context_home():
    context = {
        "title" : f"Home | {APP_NAME}",
        "links" : [{
            "text" : "Men's Fashion",
            "url" : "shop:index"
            },{
            "text" : "Womens's Fashion",
            "url" : "shop:index"
            },{
            "text" : "Babies Fashion",
            "url" : "shop:index"
            }],

        "tabs": [{
            "category" : "Men",
            "data" : "one",
            "products" : [{
                    "name": "Product One",
                    "price" : "$100.00",
                    "image" : "shop/images/placeholder.webp"
                },{
                    "name": "Product Two",
                    "price" : "$100.00",
                    "image" : "shop/images/placeholder.webp"
                },{
                    "name": "Product Three",
                    "price" : "$100.00",
                    "image" : "shop/images/placeholder.webp"
                },{
                    "name": "Product Four",
                    "price" : "$100.00",
                    "image" : "shop/images/placeholder.webp"
                },{
                    "name": "Product Five",
                    "price" : "$100.00",
                    "image" : "shop/images/placeholder.webp"
                },{
                    "name": "Product Six",
                    "price" : "$100.00",
                    "image" : "shop/images/placeholder.webp"
                }]
            },{
                "category" : "Women",
                "data" : "two",
                "products" : [{
                    "name": "Product One",
                    "price" : "$100.00",
                    "image" : "shop/images/placeholder.webp"
                },{
                    "name": "Product Two",
                    "price" : "$100.00",
                    "image" : "shop/images/placeholder.webp"
                },{
                    "name": "Product Three",
                    "price" : "$100.00",
                    "image" : "shop/images/placeholder.webp"
                },{
                    "name": "Product Four",
                    "price" : "$100.00",
                    "image" : "shop/images/placeholder.webp"
                },{
                    "name": "Product Five",
                    "price" : "$100.00",
                    "image" : "shop/images/placeholder.webp"
                }]
            }],
        "testimonials": [{
                "name" : "John Doe",
                "role" : "Developer",
                "image": "shop/images/placeholder.webp",
                "comment" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
                            Fusce pellentesque nibh neque, at volutpat dui congue ornare.\
                            Ut dignissim velit a lobortis scelerisque. Suspendisse potenti."
            },{
                "name" : "Jane Doe",
                "role" : "Designer",
                "image": "shop/images/placeholder.webp",
                "comment" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\
                            Fusce pellentesque nibh neque, at volutpat dui congue ornare.\
                            Ut dignissim velit a lobortis scelerisque. Suspendisse potenti."
            }],
        "yml" : [{
                "name": "Product One",
                "price" : "$100.00",
                "image" : "shop/images/placeholder.webp"
            },{
                "name": "Product Two",
                "price" : "$100.00",
                "image" : "shop/images/placeholder.webp"
            },{
                "name": "Product Three",
                "price" : "$100.00",
                "image" : "shop/images/placeholder.webp"
            },{
                "name": "Product Four",
                "price" : "$100.00",
                "image" : "shop/images/placeholder.webp"
            }]
        
    }
    return context
