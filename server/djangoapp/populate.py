from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Set the standard in luxury and engineering"},
        {"name": "Toyota", "description": "Reliable, efficient, and innovative global manufacturer"},
        {"name": "Honda", "description": "Exceptional reliability, performance, and fuel economy"},
        {"name": "Ford", "description": "Built tough American automotive legend"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make, created = CarMake.objects.get_or_create(
            name=data['name'],
            defaults={'description': data['description']}
        )
        car_make_instances.append(car_make)

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "X-Trail", "type": "SUV", "year": 2023, "car_make": car_make_instances[0]},
        {"name": "A-Class", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[1]},
        {"name": "Corolla", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Camry", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "RAV4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2]},
        {"name": "Civic", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Accord", "type": "SEDAN", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "CR-V", "type": "SUV", "year": 2023, "car_make": car_make_instances[3]},
        {"name": "Explorer", "type": "SUV", "year": 2023, "car_make": car_make_instances[4]},
        {"name": "Mustang", "type": "COUPE", "year": 2023, "car_make": car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.get_or_create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year']
        )
    print("Database population completed successfully.")
