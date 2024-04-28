from flask import Flask, jsonify, request
import time
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    x ={
        "name": "John the first",
        "age": 30,
        "city": "New York"
    }
    return jsonify(
        x
    )

db = {"services":[
    {
        "address": "123 Oxford Street, London, W1A 1AA",
        "id": "1",
        "name": "London Auto Clinic",
        "distance": 0.5,
        "location": "London",
        "logo": "services/one.png",
        "price": "££",
        "phone": "07770001111",
        "email": "londonautoclinic@gmail.com",
        "stars": 3
    },
    {
        "address": "456 Regent Street, London, W1B 2BB",
        "id": "2",
        "name": "City Motors",
        "distance": 2.3,
        "location": "London",
        "logo": "services/three.png",
        "price": "£££",
        "phone": "07770002222",
        "email": "citymotors@yahoo.com",
        "stars": 4
    },
    {
        "address": "789 Bond Street, London, W1C 3CC",
        "id": "3",
        "name": "London Car Care Centre",
        "distance": 4.7,
        "location": "London",
        "logo": "services/five.png",
        "price": "£",
        "phone": "07770003333",
        "email": "londoncarcare@hotmail.com",
        "stars": 2
    },
    {
        "address": "234 Piccadilly Road, London, W1D 4DD",
        "id": "4",
        "name": "West End Auto Repairs",
        "distance": 1.2,
        "location": "London",
        "logo": "services/six.png",
        "price": "££££",
        "phone": "07770004444",
        "email": "westendautorepairs@gmail.com",
        "stars": 5
    },
    {
        "address": "567 Pall Mall, London, W1E 5EE",
        "id": "5",
        "name": "Capital Garage Services",
        "distance": 3.9,
        "location": "London",
         "logo": "services/nineteen.png",
        "price": "££",
        "phone": "07770005555",
        "email": "capitalgarageservices@gmail.com",
        "stars": 3
    },
    {
        "address": "890 Coventry Street, London, W1F 6FF",
        "id": "6",
        "name": "London Vehicle Solutions",
        "distance": 6.5,
        "location": "London",
         "logo": "services/eight.png",
        "price": "£££",
        "phone": "07770006666",
        "email": "londonvehiclesolutions@hotmail.com",
        "stars": 4
    },
    {
        "address": "123 Leicester Square, London, W1G 7GG",
        "id": "7",
        "name": "Metro Car Repairs",
        "distance": 0.9,
        "location": "London",
         "logo": "services/fifteen.png",
        "price": "£",
        "phone": "07770007777",
        "email": "metrocarrepairs@gmail.com",
        "stars": 2
    },
    {
        "address": "456 Mayfair Lane, London, W1H 8HH",
        "id": "8",
        "name": "London Motor Works",
        "distance": 2.1,
        "location": "London",
         "logo": "services/thirteen.png",
        "price": "£££",
        "phone": "07770008888",
        "email": "londonmotorworks@yahoo.com",
        "stars": 4
    },
    {
        "address": "789 Soho Square, London, W1I 9II",
        "id": "9",
        "name": "Soho Auto Services",
        "distance": 5.8,
        "location": "London",
         "logo": "services/seven.png",
        "price": "£",
        "phone": "07770009999",
        "email": "sohoautoservices@gmail.com",
        "stars": 3
    },
    {
        "address": "234 Baker Street, London, W1J 1JJ",
        "id": "10",
        "name": "Baker Street Garage",
        "distance": 1.5,
        "location": "London",
        "logo": "services/two.png",
        "price": "££££",
        "phone": "07770101010",
        "email": "bakerstreetgarage@gmail.com",
        "stars": 5
    },
    {
        "address": "567 Marylebone Road, London, W1K 2KK",
        "id": "11",
        "name": "Central London Motors",
        "distance": 3.2,
        "location": "London",
         "logo": "services/nine.png",
        "price": "££",
        "phone": "07770111111",
        "email": "centrallondonmotors@gmail.com",
        "stars": 3
    },
    {
        "address": "890 Belgravia Gardens, London, W1L 3LL",
        "id": "12",
        "name": "Belgravia Auto Centre",
        "distance": 7.4,
        "location": "London",
         "logo": "services/eight.png",
        "price": "££££",
        "phone": "07770222222",
        "email": "belgraviaautocentre@hotmail.com",
        "stars": 5
    },
    {
        "address": "123 Knightsbridge Avenue, London, W1M 4MM",
        "id": "13",
        "name": "Knightsbridge Motors",
        "distance": 1.8,
        "location": "London",
         "logo": "services/eleven.png",
        "price": "££",
        "phone": "07770333333",
        "email": "knightsbridgemotors@gmail.com",
        "stars": 4
    },
    {
        "address": "456 Chelsea Lane, London, W1N 5NN",
        "id": "14",
        "name": "London Car Specialists",
        "distance": 4.0,
        "location": "London",
          "logo": "services/three.png",
        "price": "£",
        "phone": "07770444444",
        "email": "londoncarspecialists@gmail.com",
        "stars": 2
    },
    {
        "address": "789 Victoria Square, London, W1O 6OO",
        "id": "15",
        "name": "Victoria Auto Repairs",
        "distance": 9.2,
        "location": "London",
         "logo": "services/eighteen.png",
        "price": "££",
        "phone": "07770555555",
        "email": "victoriaautorepairs@gmail.com",
        "stars": 3
    },
    {
        "address": "234 Westminster Road, London, W1P 7PP",
        "id": "16",
        "name": "Westminster Motors",
        "distance": 5.5,
        "location": "London",
         "logo": "services/ten.png",
        "price": "££££",
        "phone": "07770666666",
        "email": "westminstermotors@hotmail.com",
        "stars": 5
    },
    {
        "address": "567 Camden Street, London, W1Q 8QQ",
        "id": "17",
        "name": "Camden Car Care",
        "distance": 3.0,
        "location": "London",
         "logo": "services/seven.png",
        "price": "£",
        "phone": "07770777777",
        "email": "camdencarcare@gmail.com",
        "stars": 2
    },
    {
        "address": "890 Hackney Road, London, W1R 9RR",
        "id": "18",
        "name": "Hackney Auto Specialists",
        "distance": 6.8,
        "location": "London",
        "logo": "services/five.png",
        "price": "£££",
        "phone": "07770888888",
        "email": "hackneyautospecialists@yahoo.com",
        "stars": 4
    },
    {
        "address": "123 Shoreditch Lane, London, W1S 1SS",
        "id": "19",
        "name": "SOS Garage",
        "distance": 2.4,
        "location": "London",
        "logo": "services/four.png",
        "price": "££",
        "phone": "07770999999",
        "email": "sosgarage@gmail.com",
        "stars": 3
    },
    {
        "address": "456 Islington Avenue, London, W1T 4TT",
        "id": "20",
        "name": "Islington Car Clinic",
        "distance": 4.3,
        "location": "London",
         "logo": "services/thirteen.png",
        "price": "££££",
        "phone": "07771010101",
        "email": "islingtoncarclinic@gmail.com",
        "stars": 5
    },
    {
        "address": "123 Broad Street, Birmingham, B1 1AA",
        "id": "21",
        "name": "Birmingham Auto Experts",
        "distance": 0.8,
        "location": "Birmingham",
         "logo": "services/one.png",
        "price": "££",
        "phone": "07772111111",
        "email": "birminghamautoexperts@gmail.com",
        "stars": 3
    },
    {
        "address": "456 High Street, Birmingham, B1 2BB",
        "id": "22",
        "name": "Midland Motors",
        "distance": 5.2,
        "location": "Birmingham",
         "logo": "services/two.png",
        "price": "£££",
        "phone": "07772222222",
        "email": "midlandmotors@yahoo.com",
        "stars": 4
    },
    {
        "address": "789 Commercial Road, Birmingham, B1 3CC",
        "id": "23",
        "name": "City Car Care Birmingham",
        "distance": 4.7,
        "location": "Birmingham",
         "logo": "services/five.png",
        "price": "£",
        "phone": "07772333333",
        "email": "citycarcarebirmingham@hotmail.com",
        "stars": 2
    },
    {
        "address": "234 Aston Lane, Birmingham, B1 4DD",
        "id": "24",
        "name": "Aston Auto Repairs",
        "distance": 1.2,
        "location": "Birmingham",
         "logo": "services/seven.png",
        "price": "££££",
        "phone": "07772444444",
        "email": "astonautorepairs@gmail.com",
        "stars": 5
    },
    {
        "address": "567 Digbeth Road, Birmingham, B1 5EE",
        "id": "25",
        "name": "Digbeth Garage Services",
        "distance": 3.9,
        "location": "Birmingham",
         "logo": "services/eight.png",
        "price": "££",
        "phone": "07772555555",
        "email": "digbethgarageservices@gmail.com",
        "stars": 3
    },
    {
        "address": "890 Stratford Street, Birmingham, B1 6FF",
        "id": "26",
        "name": "Birmingham Vehicle Repairs",
        "distance": 6.5,
        "location": "Birmingham",
        "logo": "services/two.png",
        "price": "£££",
        "phone": "07772666666",
        "email": "birminghamvehiclerepairs@hotmail.com",
        "stars": 4
    },
    {
        "address": "123 Aston University Road, Birmingham, B1 7GG",
        "id": "27",
        "name": "Aston Auto Care",
        "distance": 0.9,
        "location": "Birmingham",
          "logo": "services/three.png",
        "price": "£",
        "phone": "07772777777",
        "email": "astonautocare@gmail.com",
        "stars": 2
    },
    {
        "address": "456 Bullring Lane, Birmingham, B1 8HH",
        "id": "28",
        "name": "Bullring Motors",
        "distance": 2.1,
        "location": "Birmingham",
         "logo": "services/nineteen.png",
        "price": "£££",
        "phone": "07772888888",
        "email": "bullringmotors@yahoo.com",
        "stars": 4
    },
    {
        "address": "789 Edgbaston Square, Birmingham, B1 9II",
        "id": "29",
        "name": "Edgbaston Auto Specialists",
        "distance": 5.8,
        "location": "Birmingham",
         "logo": "services/seven.png",
        "price": "£",
        "phone": "07772999999",
        "email": "edgbastonautospecialists@gmail.com",
        "stars": 3
    },
    {
        "address": "234 Solihull Road, Birmingham, B1 10JJ",
        "id": "30",
        "name": "Solihull Car Clinic",
        "distance": 1.5,
        "location": "Birmingham",
        "logo": "services/six.png",
        "price": "££££",
        "phone": "07773010101",
        "email": "solihullcarclinic@gmail.com",
        "stars": 5
    },
    {
        "address": "567 Selly Oak Avenue, Birmingham, B1 11KK",
        "id": "31",
        "name": "Oak Auto Garage",
        "distance": 3.2,
        "location": "Birmingham",
         "logo": "services/eleven.png",
        "price": "££",
        "phone": "07773111111",
        "email": "oakautogarage@gmail.com",
        "stars": 3
    },
    {
        "address": "890 Bournville Lane, Birmingham, B1 12LL",
        "id": "32",
        "name": "Bournville Motors",
        "distance": 7.4,
        "location": "Birmingham",
         "logo": "services/ten.png",
        "price": "££££",
        "phone": "07773222222",
        "email": "bournvillemotors@hotmail.com",
        "stars": 5
    },
    {
        "address": "123 Harborne Road, Birmingham, B1 13MM",
        "id": "33",
        "name": "Harborne Car Repairs",
        "distance": 1.8,
        "location": "Birmingham",
        "logo": "services/four.png",
        "price": "££",
        "phone": "07773333333",
        "email": "harbornecarrepairs@gmail.com",
        "stars": 4
    },
    {
        "address": "456 Moseley Street, Birmingham, B1 14NN",
        "id": "34",
        "name": "Moseley Auto Centre",
        "distance": 4.0,
        "location": "Birmingham",
         "logo": "services/two.png",
        "price": "£",
        "phone": "07773444444",
        "email": "moseleyautocentre@gmail.com",
        "stars": 2
    },
    {
        "address": "789 Perry Barr Square, Birmingham, B1 15OO",
        "id": "35",
        "name": "Perry Barr Garage",
        "distance": 9.2,
        "location": "Birmingham",
         "logo": "services/seventeen.png",
        "price": "££",
        "phone": "07773555555",
        "email": "perrybarrgarage@gmail.com",
        "stars": 3
    },
    {
        "address": "234 Handsworth Road, Birmingham, B1 16PP",
        "id": "36",
        "name": "Handsworth Car Specialists",
        "distance": 5.5,
        "location": "Birmingham",
        "logo": "services/five.png",
        "price": "££££",
        "phone": "07773666666",
        "email": "handsworthcarspecialists@hotmail.com",
        "stars": 5
    },
    {
        "address": "567 Erdington Lane, Birmingham, B1 17QQ",
        "id": "37",
        "name": "Erdington Auto Solutions",
        "distance": 3.0,
        "location": "Birmingham",
          "logo": "services/three.png",
        "price": "£",
        "phone": "07773777777",
        "email": "erdingtonautosolutions@gmail.com",
        "stars": 2
    },
    {
        "address": "890 Sutton Coldfield Road, Birmingham, B1 18RR",
        "id": "38",
        "name": "Sutton Coldfield Car Clinic",
        "distance": 6.8,
        "location": "Birmingham",
         "logo": "services/sixteen.png",
        "price": "£££",
        "phone": "07773888888",
        "email": "suttoncoldfieldcarclinic@yahoo.com",
        "stars": 4
    },
    {
        "address": "123 Kings Heath Avenue, Birmingham, B1 19SS",
        "id": "39",
        "name": "Kings Heath Motors",
        "distance": 2.4,
        "location": "Birmingham",
         "logo": "services/twenty.png",
        "price": "££",
        "phone": "07773999999",
        "email": "kingsheathmotors@gmail.com",
        "stars": 3
    },
    {
        "address": "456 Aston Expressway, Birmingham, B1 20TT",
        "id": "40",
        "name": "Aston Car Clinic",
        "distance": 4.3,
        "location": "Birmingham",
         "logo": "services/seven.png",
        "price": "££££",
        "phone": "07774010101",
        "email": "astoncarclinic@gmail.com",
        "stars": 5
    },
    {
        "address": "123 Deansgate, Manchester, M1 1AA",
        "id": "41",
        "name": "Northern Auto Repairs",
        "distance": 0.6,
        "location": "Manchester",
        "logo": "services/one.png",
        "price": "££",
        "phone": "07774111111",
        "email": "northernautorepairs@gmail.com",
        "stars": 3
    },
    {
        "address": "456 Oxford Road, Manchester, M1 2BB",
        "id": "42",
        "name": "City Centre Motors",
        "distance": 4.2,
        "location": "Manchester",
        "logo": "services/six.png",
        "price": "£££",
        "phone": "07774222222",
        "email": "citycentremotors@yahoo.com",
        "stars": 4
    },
    {
        "address": "789 Piccadilly Gardens, Manchester, M1 3CC",
        "id": "43",
        "name": "Manchester Car Clinic",
        "distance": 3.9,
        "location": "Manchester",
         "logo": "services/five.png",
        "price": "£",
        "phone": "07774333333",
        "email": "manchestercarclinic@hotmail.com",
        "stars": 2
    },
    {
        "address": "234 Trafford Park, Manchester, M1 4DD",
        "id": "44",
        "name": "Trafford Auto Care",
        "distance": 1.3,
        "location": "Manchester",
         "logo": "services/five.png",
        "price": "££££",
        "phone": "07774444444",
        "email": "traffordautocare@gmail.com",
        "stars": 5
    },
    {
        "address": "567 Salford Quays, Manchester, M1 5EE",
        "id": "45",
        "name": "Quayside Garage",
        "distance": 3.5,
        "location": "Manchester",
         "logo": "services/thirteen.png",
        "price": "££",
        "phone": "07774555555",
        "email": "quaysidegarage@gmail.com",
        "stars": 3
    },
    {
        "address": "890 Ancoats Street, Manchester, M1 6FF",
        "id": "46",
        "name": "Manchester Vehicle Repairs",
        "distance": 7.1,
        "location": "Manchester",
         "logo": "services/eleven.png",
        "price": "£££",
        "phone": "07774666666",
        "email": "manchestervehiclerepairs@hotmail.com",
        "stars": 4
    },
    {
        "address": "123 Castlefield Road, Manchester, M1 7GG",
        "id": "47",
        "name": "Castlefield Auto Centre",
        "distance": 1.1,
        "location": "Manchester",
        "logo": "services/two.png",
        "price": "£",
        "phone": "07774777777",
        "email": "castlefieldautocentre@gmail.com",
        "stars": 2
    },
    {
        "address": "456 Northern Quarter, Manchester, M1 8HH",
        "id": "48",
        "name": "Northern Quarter Motors",
        "distance": 2.5,
        "location": "Manchester",
         "logo": "services/sixteen.png",
        "price": "£££",
        "phone": "07774888888",
        "email": "northernquartermotors@yahoo.com",
        "stars": 4
    },
    {
        "address": "789 Chorlton Road, Manchester, M1 9II",
        "id": "49",
        "name": "Chorlton Car Specialists",
        "distance": 6.4,
        "location": "Manchester",
          "logo": "services/three.png",
        "price": "£",
        "phone": "07774999999",
        "email": "chorltoncarspecialists@gmail.com",
        "stars": 3
    },
    {
        "address": "234 Didsbury Lane, Manchester, M1 10JJ",
        "id": "50",
        "name": "Didsbury Auto Clinic",
        "distance": 2.0,
        "location": "Manchester",
         "logo": "services/fourteen.png",
        "price": "££££",
        "phone": "07775010101",
        "email": "didsburyautoclinic@gmail.com",
        "stars": 5
    },
    {
        "address": "567 Rusholme Avenue, Manchester, M1 11KK",
        "id": "51",
        "name": "Rusholme Car Repairs",
        "distance": 4.1,
        "location": "Manchester",
         "logo": "services/four.png",
        "price": "££",
        "phone": "07775111111",
        "email": "rusholmecarrepairs@gmail.com",
        "stars": 3
    },
    {
        "address": "890 Fallowfield Square, Manchester, M1 12LL",
        "id": "52",
        "name": "Fallowfield Garage",
        "distance": 8.2,
        "location": "Manchester",
        "logo": "services/five.png",
        "price": "££££",
        "phone": "07775222222",
        "email": "fallowfieldgarage@hotmail.com",
        "stars": 5
    },
    {
        "address": "123 Hulme Road, Manchester, M1 13MM",
        "id": "53",
        "name": "Hulme Auto Works",
        "distance": 1.7,
        "location": "Manchester",
         "logo": "services/two.png",
        "price": "££",
        "phone": "07775333333",
        "email": "hulmeautoworks@gmail.com",
        "stars": 4
    },
    {
        "address": "456 Cheetham Hill Lane, Manchester, M1 14NN",
        "id": "54",
        "name": "Cheetham Hill Motors",
        "distance": 3.8,
        "location": "Manchester",
        "logo": "services/four.png",
        "price": "£",
        "phone": "07775444444",
        "email": "cheethamhillmotors@gmail.com",
        "stars": 2
    },
    {
        "address": "789 Whalley Range Square, Manchester, M1 15OO",
        "id": "55",
        "name": "Whalley Range Auto Services",
        "distance": 9.5,
        "location": "Manchester",
         "logo": "services/seven.png",
        "price": "££",
        "phone": "07775555555",
        "email": "whalleyrangeautoservices@gmail.com",
        "stars": 3
    },
    {
        "address": "234 Longsight Road, Manchester, M1 16PP",
        "id": "56",
        "name": "Longsight Car Repairs",
        "distance": 4.5,
        "location": "Manchester",
         "logo": "services/twelve.png",
        "price": "££££",
        "phone": "07775666666",
        "email": "longsightcarrepairs@hotmail.com",
        "stars": 5
    },
    {
        "address": "567 Gorton Lane, Manchester, M1 17QQ",
        "id": "57",
        "name": "Gorton Auto Solutions",
        "distance": 3.3,
        "location": "Manchester",
         "logo": "services/fifteen.png",
        "price": "£",
        "phone": "07775777777",
        "email": "gortonautosolutions@gmail.com",
        "stars": 2
    },
    {
        "address": "890 Prestwich Road, Manchester, M1 18RR",
        "id": "58",
        "name": "Prestwich Car Clinic",
        "distance": 7.0,
        "location": "Manchester",
         "logo": "services/seven.png",
        "price": "£££",
        "phone": "07775888888",
        "email": "prestwichcarclinic@yahoo.com",
        "stars": 4
    },
    {
        "address": "123 Withington Avenue, Manchester, M1 19SS",
        "id": "59",
        "name": "Withington Motors",
        "distance": 2.9,
        "location": "Manchester",
         "logo": "services/five.png",
        "price": "££",
        "phone": "07775999999",
        "email": "withingtonmotors@gmail.com",
        "stars": 3
    },
    {
        "address": "456 Blackley Lane, Manchester, M1 20TT",
        "id": "60",
        "name": "Blackley Car Clinic",
        "distance": 4.8,
        "location": "Manchester",
        "logo": "services/six.png",
        "price": "££££",
        "phone": "07776010101",
        "email": "blackleycarclinic@gmail.com",
        "stars": 5
    },
     {
        "address": "123 Minster Street, York, YO1 1AA",
        "id": "61",
        "name": "Minster City Garage",
        "distance": 0.4,
        "location": "York",
         "logo": "services/two.png",
        "price": "££",
        "phone": "07776111111",
        "email": "minstercitygarage@gmail.com",
        "stars": 3
    },
    {
        "address": "456 Micklegate Road, York, YO1 2BB",
        "id": "62",
        "name": "Micklegate Motors",
        "distance": 1.8,
        "location": "York",
         "logo": "services/eighteen.png",
        "price": "£££",
        "phone": "07776222222",
        "email": "micklegatemotors@yahoo.com",
        "stars": 4
    },
    {
        "address": "789 Shambles Lane, York, YO1 3CC",
        "id": "63",
        "name": "Shambles Car Repairs",
        "distance": 1.5,
        "location": "York",
         "logo": "services/nineteen.png",
        "price": "£",
        "phone": "07776333333",
        "email": "shamblescarrepairs@hotmail.com",
        "stars": 2
    },
    {
        "address": "234 Bootham Crescent, York, YO1 4DD",
        "id": "64",
        "name": "Bootham Auto Services",
        "distance": 0.9,
        "location": "York",
         "logo": "services/fourteen.png",
        "price": "££££",
        "phone": "07776444444",
        "email": "boothamautoservices@gmail.com",
        "stars": 5
    },
    {
        "address": "567 Walmgate Avenue, York, YO1 5EE",
        "id": "65",
        "name": "Walmgate Garage",
        "distance": 2.3,
        "location": "York",
         "logo": "services/eight.png",
        "price": "££",
        "phone": "07776555555",
        "email": "walmgategarage@gmail.com",
        "stars": 3
    },
    {
        "address": "890 Fossgate Street, York, YO1 6FF",
        "id": "66",
        "name": "Fossgate Vehicle Repairs",
        "distance": 3.8,
        "location": "York",
          "logo": "services/three.png",
        "price": "£££",
        "phone": "07776666666",
        "email": "fossgatevehiclerepairs@hotmail.com",
        "stars": 4
    },
    {
        "address": "123 Coney Street, York, YO1 7GG",
        "id": "67",
        "name": "Coney Street Auto Centre",
        "distance": 0.7,
        "location": "York",
         "logo": "services/three.png",
        "price": "£",
        "phone": "07776777777",
        "email": "coneystreetautocentre@gmail.com",
        "stars": 2
    },
    {
        "address": "456 Gillygate Lane, York, YO1 8HH",
        "id": "68",
        "name": "Gillygate Motors",
        "distance": 1.2,
        "location": "York",
         "logo": "services/seven.png",
        "price": "£££",
        "phone": "07776888888",
        "email": "gillygatemotors@yahoo.com",
        "stars": 4
    },
    {
        "address": "789 Fulford Road, York, YO1 9II",
        "id": "69",
        "name": "Fulford Car Specialists",
        "distance": 4.5,
        "location": "York",
        "logo": "services/two.png",
        "price": "£",
        "phone": "07776999999",
        "email": "fulfordcarspecialists@gmail.com",
        "stars": 3
    },
    {
        "address": "234 Heworth Lane, York, YO1 10JJ",
        "id": "70",
        "name": "Heworth Auto Clinic",
        "distance": 2.6,
        "location": "York",
         "logo": "services/five.png",
        "price": "££££",
        "phone": "07777010101",
        "email": "heworthautoclinic@gmail.com",
        "stars": 5
    },
    {
        "address": "567 Clifton Avenue, York, YO1 11KK",
        "id": "71",
        "name": "Clifton Car Repairs",
        "distance": 3.1,
        "location": "York",
        "logo": "services/four.png",
        "price": "££",
        "phone": "07777111111",
        "email": "cliftoncarrepairs@gmail.com",
        "stars": 3
    },
    {
        "address": "890 Acomb Square, York, YO1 12LL",
        "id": "72",
        "name": "Acomb Auto Centre",
        "distance": 5.2,
        "location": "York",
         "logo": "services/twenty.png",
        "price": "££££",
        "phone": "07777222222",
        "email": "acombautocentre@hotmail.com",
        "stars": 5
    },
    {
        "address": "123 Haxby Avenue, York, YO1 13MM",
        "id": "73",
        "name": "Haxby Car Care",
        "distance": 1.3,
        "location": "York",
        "logo": "services/five.png",
        "price": "££",
        "phone": "07777333333",
        "email": "haxbycarcare@gmail.com",
        "stars": 4
    },
    {
        "address": "456 Osbaldwick Street, York, YO1 14NN",
        "id": "74",
        "name": "Osbaldwick Auto Services",
        "distance": 2.8,
        "location": "York",
        "logo": "services/one.png",
        "price": "£",
        "phone": "07777444444",
        "email": "osbaldwickautoservices@gmail.com",
        "stars": 2
    },
    {
        "address": "789 Bishopthorpe Road, York, YO1 15OO",
        "id": "75",
        "name": "Bishopthorpe Garage",
        "distance": 6.1,
        "location": "York",
          "logo": "services/three.png",
        "price": "££",
        "phone": "07777555555",
        "email": "bishopthorpegarage@gmail.com",
        "stars": 3
    },
    {
        "address": "234 Holgate Lane, York, YO1 16PP",
        "id": "76",
        "name": "Holgate Car Clinic",
        "distance": 3.4,
        "location": "York",
         "logo": "services/six.png",
        "price": "££££",
        "phone": "07777666666",
        "email": "holgatecarclinic@hotmail.com",
        "stars": 5
    },
    {
        "address": "567 Huntington Lane, York, YO1 17QQ",
        "id": "77",
        "name": "Huntington Auto Solutions",
        "distance": 2.2,
        "location": "York",
         "logo": "services/eight.png",
        "price": "£",
        "phone": "07777777777",
        "email": "huntingtonautosolutions@gmail.com",
        "stars": 2
    },
    {
        "address": "890 Dunnington Road, York, YO1 18RR",
        "id": "78",
        "name": "Dunnington Car Clinic",
        "distance": 5.7,
        "location": "York",
        "logo": "services/six.png",
        "price": "£££",
        "phone": "07777888888",
        "email": "dunningtoncarclinic@yahoo.com",
        "stars": 4
    },
    {
        "address": "123 Poppleton Avenue, York, YO1 19SS",
        "id": "79",
        "name": "Poppleton Motors",
        "distance": 3.0,
        "location": "York",
         "logo": "services/five.png",
        "price": "££",
        "phone": "07777999999",
        "email": "poppletonmotors@gmail.com",
        "stars": 3
    },
    {
        "address": "456 Rawcliffe Lane, York, YO1 20TT",
        "id": "80",
        "name": "Rawcliffe Car Care",
        "distance": 4.2,
        "location": "York",
         "logo": "services/four.png",
        "price": "££££",
        "phone": "07778010101",
        "email": "rawcliffecarcare@gmail.com",
        "stars": 5
    },
     {
        "address": "123 Briggate, Leeds, LS1 1AA",
        "id": "81",
        "name": "Briggate Auto Centre",
        "distance": 0.5,
        "location": "Leeds",
         "logo": "services/five.png",
        "price": "££",
        "phone": "07778111111",
        "email": "briggateautocentre@gmail.com",
        "stars": 3
    },
    {
        "address": "456 Headrow Avenue, Leeds, LS1 2BB",
        "id": "82",
        "name": "Headrow Motors",
        "distance": 1.9,
        "location": "Leeds",
        "logo": "services/four.png",
        "price": "£££",
        "phone": "07778222222",
        "email": "headrowmotors@yahoo.com",
        "stars": 4
    },
    {
        "address": "789 Kirkgate Lane, Leeds, LS1 3CC",
        "id": "83",
        "name": "Kirkgate Car Repairs",
        "distance": 1.3,
        "location": "Leeds",
         "logo": "services/fourteen.png",
        "price": "£",
        "phone": "07778333333",
        "email": "kirkgatecarrepairs@hotmail.com",
        "stars": 2
    },
    {
        "address": "234 Holbeck Crescent, Leeds, LS1 4DD",
        "id": "84",
        "name": "Holbeck Auto Services",
        "distance": 0.8,
        "location": "Leeds",
         "logo": "services/nine.png",
        "price": "££££",
        "phone": "07778444444",
        "email": "holbeckautoservices@gmail.com",
        "stars": 5
    },
    {
        "address": "567 Roundhay Road, Leeds, LS1 5EE",
        "id": "85",
        "name": "Roundhay Garage",
        "distance": 2.4,
        "location": "Leeds",
         "logo": "services/nineteen.png",
        "price": "££",
        "phone": "07778555555",
        "email": "roundhaygarage@gmail.com",
        "stars": 3
    },
    {
        "address": "890 Hunslet Street, Leeds, LS1 6FF",
        "id": "86",
        "name": "Hunslet Vehicle Repairs",
        "distance": 3.6,
        "location": "Leeds",
         "logo": "services/six.png",
        "price": "£££",
        "phone": "07778666666",
        "email": "hunsletvehiclerepairs@hotmail.com",
        "stars": 4
    },
    {
        "address": "123 Armley Road, Leeds, LS1 7GG",
        "id": "87",
        "name": "Armley Auto Centre",
        "distance": 0.9,
        "location": "Leeds",
         "logo": "services/ten.png",
        "price": "£",
        "phone": "07778777777",
        "email": "armleyautocentre@gmail.com",
        "stars": 2
    },
    {
        "address": "456 Chapel Allerton Lane, Leeds, LS1 8HH",
        "id": "88",
        "name": "Chapel Allerton Motors",
        "distance": 1.5,
        "location": "Leeds",
        "logo": "services/one.png",
        "price": "£££",
        "phone": "07778888888",
        "email": "chapelallertonmotors@yahoo.com",
        "stars": 4
    },
    {
        "address": "789 Bramley Road, Leeds, LS1 9II",
        "id": "89",
        "name": "Bramley Car Specialists",
        "distance": 4.2,
        "location": "Leeds",
         "logo": "services/seven.png",
        "price": "£",
        "phone": "07778999999",
        "email": "bramleycarspecialists@gmail.com",
        "stars": 3
    },
    {
        "address": "234 Moortown Lane, Leeds, LS1 10JJ",
        "id": "90",
        "name": "Moortown Auto Clinic",
        "distance": 2.1,
        "location": "Leeds",
        "logo": "services/five.png",
        "price": "££££",
        "phone": "07779010101",
        "email": "moortownautoclinic@gmail.com",
        "stars": 5
    },
    {
        "address": "567 Seacroft Avenue, Leeds, LS1 11KK",
        "id": "91",
        "name": "Seacroft Car Repairs",
        "distance": 3.1,
        "location": "Leeds",
        "logo": "services/six.png",
        "price": "££",
        "phone": "07779111111",
        "email": "seacroftcarrepairs@gmail.com",
        "stars": 3
    },
    {
        "address": "890 Pudsey Square, Leeds, LS1 12LL",
        "id": "92",
        "name": "Pudsey Auto Centre",
        "distance": 6.3,
        "location": "Leeds",
         "logo": "services/twenty.png",
        "price": "££££",
        "phone": "07779222222",
        "email": "pudseyautocentre@hotmail.com",
        "stars": 5
    },
    {
        "address": "123 Harehills Avenue, Leeds, LS1 13MM",
        "id": "93",
        "name": "Harehills Car Care",
        "distance": 1.2,
        "location": "Leeds",
         "logo": "services/two.png",
        "price": "££",
        "phone": "07779333333",
        "email": "harehillscarcare@gmail.com",
        "stars": 4
    },
    {
        "address": "456 Beeston Lane, Leeds, LS1 14NN",
        "id": "94",
        "name": "Beeston Auto Services",
        "distance": 3.4,
        "location": "Leeds",
         "logo": "services/three.png",
        "price": "£",
        "phone": "07779444444",
        "email": "beestonautoservices@gmail.com",
        "stars": 2
    },
    {
        "address": "789 Morley Road, Leeds, LS1 15OO",
        "id": "95",
        "name": "Morley Garage",
        "distance": 5.9,
        "location": "Leeds",
        "logo": "services/two.png",
        "price": "££",
        "phone": "07779555555",
        "email": "morleygarage@gmail.com",
        "stars": 3
    },
    {
        "address": "234 Roundhay Lane, Leeds, LS1 16PP",
        "id": "96",
        "name": "Roundhay Car Clinic",
        "distance": 3.2,
        "location": "Leeds",
         "logo": "services/sixteen.png",
        "price": "££££",
        "phone": "07779666666",
        "email": "roundhaycarclinic@hotmail.com",
        "stars": 5
    },
    {
        "address": "567 Garforth Lane, Leeds, LS1 17QQ",
        "id": "97",
        "name": "Garforth Auto Solutions",
        "distance": 2.8,
        "location": "Leeds",
         "logo": "services/seventeen.png",
        "price": "£",
        "phone": "07779777777",
        "email": "garforthautosolutions@gmail.com",
        "stars": 2
    },
    {
        "address": "890 Rothwell Road, Leeds, LS1 18RR",
        "id": "98",
        "name": "Rothwell Car Clinic",
        "distance": 6.1,
        "location": "Leeds",
        "logo": "services/four.png",
        "price": "£££",
        "phone": "07779888888",
        "email": "rothwellcarclinic@yahoo.com",
        "stars": 4
    },
    {
        "address": "123 Armley Ridge, Leeds, LS1 19SS",
        "id": "99",
        "name": "Armley Ridge Motors",
        "distance": 3.3,
        "location": "Leeds",
         "logo": "services/eighteen.png",
        "price": "££",
        "phone": "07779999999",
        "email": "armleyridgemotors@gmail.com",
        "stars": 3
    },
    {
        "address": "456 Cross Gates Lane, Leeds, LS1 20TT",
        "id": "100",
        "name": "Cross Gates Car Care",
        "distance": 4.7,
        "location": "Leeds",
         "logo": "services/nineteen.png",
        "price": "££££",
        "phone": "07780010101",
        "email": "crossgatescarcare@gmail.com",
        "stars": 5
    },
     {
        "address": "123 High Street, Coventry, CV1 1AA",
        "id": "101",
        "name": "City Centre Auto Repairs",
        "distance": 0.6,
        "location": "Coventry",
        "logo": "services/one.png",
        "price": "££",
        "phone": "07780111111",
        "email": "citycentreautorepairs@gmail.com",
        "stars": 3
    },
    {
        "address": "456 Foleshill Road, Coventry, CV1 2BB",
        "id": "102",
        "name": "Foleshill Motors",
        "distance": 2.4,
        "location": "Coventry",
         "logo": "services/five.png",
        "price": "£££",
        "phone": "07780222222",
        "email": "foleshillmotors@yahoo.com",
        "stars": 4
    },
    {
        "address": "789 Broadgate Lane, Coventry, CV1 3CC",
        "id": "103",
        "name": "Broadgate Car Repairs",
        "distance": 1.8,
        "location": "Coventry",
         "logo": "services/seven.png",
        "price": "£",
        "phone": "07780333333",
        "email": "broadgatecarrepairs@hotmail.com",
        "stars": 2
    },
    {
        "address": "234 Earlsdon Crescent, Coventry, CV1 4DD",
        "id": "104",
        "name": "Earlsdon Auto Services",
        "distance": 1.2,
        "location": "Coventry",
         "logo": "services/three.png",
        "price": "££££",
        "phone": "07780444444",
        "email": "earlsdonautoservices@gmail.com",
        "stars": 5
    },
    {
        "address": "567 Canley Road, Coventry, CV1 5EE",
        "id": "105",
        "name": "Canley Garage",
        "distance": 3.5,
        "location": "Coventry",
          "logo": "services/three.png",
        "price": "££",
        "phone": "07780555555",
        "email": "canleygarage@gmail.com",
        "stars": 3
    },
    {
        "address": "890 Wyken Street, Coventry, CV1 6FF",
        "id": "106",
        "name": "Wyken Vehicle Repairs",
        "distance": 4.2,
        "location": "Coventry",
        "logo": "services/five.png",
        "price": "£££",
        "phone": "07780666666",
        "email": "wykenvehiclerepairs@hotmail.com",
        "stars": 4
    },
    {
        "address": "123 Cheylesmore Road, Coventry, CV1 7GG",
        "id": "107",
        "name": "Cheylesmore Auto Centre",
        "distance": 1.5,
        "location": "Coventry",
        "logo": "services/six.png",
        "price": "£",
        "phone": "07780777777",
        "email": "cheylesmoreautocentre@gmail.com",
        "stars": 2
    },
    {
        "address": "456 Tile Hill Lane, Coventry, CV1 8HH",
        "id": "108",
        "name": "Tile Hill Motors",
        "distance": 3.0,
        "location": "Coventry",
         "logo": "services/ten.png",
        "price": "£££",
        "phone": "07780888888",
        "email": "tilehillmotors@yahoo.com",
        "stars": 4
    },
    {
        "address": "789 Radford Road, Coventry, CV1 9II",
        "id": "109",
        "name": "Radford Car Specialists",
        "distance": 4.8,
        "location": "Coventry",
         "logo": "services/sixteen.png",
        "price": "£",
        "phone": "07780999999",
        "email": "radfordcarspecialists@gmail.com",
        "stars": 3
    },
    {
        "address": "234 Spon End Lane, Coventry, CV1 10JJ",
        "id": "110",
        "name": "Spon End Auto Clinic",
        "distance": 2.7,
        "location": "Coventry",
         "logo": "services/nineteen.png",
        "price": "££££",
        "phone": "07781010101",
        "email": "sponendautoclinic@gmail.com",
        "stars": 5
    },
    {
        "address": "567 Allesley Avenue, Coventry, CV1 11KK",
        "id": "111",
        "name": "Allesley Car Repairs",
        "distance": 5.1,
        "location": "Coventry",
         "logo": "services/five.png",
        "price": "££",
        "phone": "07781111111",
        "email": "allesleycarrepairs@gmail.com",
        "stars": 3
    },
    {
        "address": "890 Keresley Road, Coventry, CV1 12LL",
        "id": "112",
        "name": "Keresley Auto Centre",
        "distance": 3.3,
        "location": "Coventry",
         "logo": "services/twenty.png",
        "price": "££££",
        "phone": "07781222222",
        "email": "keresleyautocentre@hotmail.com",
        "stars": 5
    },
    {
        "address": "123 Longford Avenue, Coventry, CV1 13MM",
        "id": "113",
        "name": "Longford Car Care",
        "distance": 2.0,
        "location": "Coventry",
         "logo": "services/eleven.png",
        "price": "££",
        "phone": "07781333333",
        "email": "longfordcarcare@gmail.com",
        "stars": 4
    },
    {
        "address": "456 Whitley Lane, Coventry, CV1 14NN",
        "id": "114",
        "name": "Whitley Auto Services",
        "distance": 4.4,
        "location": "Coventry",
        "logo": "services/seven.png",
        "price": "£",
        "phone": "07781444444",
        "email": "whitleyautoservices@gmail.com",
        "stars": 2
    },
    {
        "address": "789 Earlsdon Avenue, Coventry, CV1 15OO",
        "id": "115",
        "name": "Earlsdon Garage",
        "distance": 6.0,
        "location": "Coventry",
        "logo": "services/six.png",
        "price": "££",
        "phone": "07781555555",
        "email": "earlsdongarage@gmail.com",
        "stars": 3
    },
    {
        "address": "234 Coundon Lane, Coventry, CV1 16PP",
        "id": "116",
        "name": "Coundon Car Clinic",
        "distance": 3.6,
        "location": "Coventry",
        "logo": "services/five.png",
        "price": "££££",
        "phone": "07781666666",
        "email": "coundoncarclinic@hotmail.com",
        "stars": 5
    },
    {
        "address": "567 Canley Lane, Coventry, CV1 17QQ",
        "id": "117",
        "name": "Canley Auto Solutions",
        "distance": 2.3,
        "location": "Coventry",
        "logo": "services/four.png",
        "price": "£",
        "phone": "07781777777",
        "email": "canleyautosolutions@gmail.com",
        "stars": 2
    },
    {
        "address": "890 Chapelfields Road, Coventry, CV1 18RR",
        "id": "118",
        "name": "Chapelfields Car Clinic",
        "distance": 5.3,
        "location": "Coventry",
        "logo": "services/two.png",
        "price": "£££",
        "phone": "07781888888",
        "email": "chapelfieldscarclinic@yahoo.com",
        "stars": 4
    },
    {
        "address": "123 Hillfields Avenue, Coventry, CV1 19SS",
        "id": "119",
        "name": "Hillfields Motors",
        "distance": 3.1,
        "location": "Coventry",
        "logo": "services/three.png",
        "price": "££",
        "phone": "07781999999",
        "email": "hillfieldsmotors@gmail.com",
        "stars": 3
    },
    {
        "address": "456 Radford Lane, Coventry, CV1 20TT",
        "id": "120",
        "name": "Radford Car Care",
        "distance": 4.7,
        "location": "Coventry",
        "logo": "services/one.png",
        "price": "££££",
        "phone": "07782010101",
        "email": "radfordcarcare@gmail.com",
        "stars": 5
    }
]
,
    "booked": []}


@app.route('/list', methods=['GET'])
def list():
    return jsonify(db)

@app.route('/getbyid/<id>', methods=['GET'])
def getbyid(id):
    service =  {
        key: [item for item in value if item.get("id") == id]
        for key, value in db.items()}
    return jsonify(service["services"][0])


@app.route('/filter', methods=['POST'])
def filter():
    data=request.json

    filtered_dict = {
    key: [item for item in value if item.get("location") == data["location"] and  item.get("price") in data["price"] and  item.get("stars") in data["stars"]]
    for key, value in db.items()
}


    # filtered_dict = {key: value for key, value in db.items() if value.get("location") == data["location"]}
    return jsonify(filtered_dict)


@app.route('/add', methods=['POST'])
def add():
    data = request.json
    db["booked"].append(data)
    # data["id"] = str(int(time.time()))
    # db[data["id"]] = data
    # return jsonify(db)
    return jsonify(data["bookingId"])

@app.route('/getbookingbyid/<id>', methods=['GET'])
def getbookingbyid(id):
    booking =  {
        key: [item for item in value if item.get("bookingId") == id]
        for key, value in db.items()}
    return jsonify(booking["booked"][0])


@app.route('/getbookings', methods=['GET'])
def getbookings():
    return jsonify(db["booked"])

@app.route('/update/<id>', methods=['POST'])
def update(id):

    for item in(db["booked"]):
        if item.get("bookingId") == id:
            i=db["booked"].index(item)
            break

    data = request.json
    db["booked"][i] = data
    return jsonify(db["booked"])

@app.route('/remove/<id>', methods=['POST'])
def remove(id): 
    for item in(db["booked"]):
        if item.get("bookingId") == id:
            i=db["booked"].index(item)
            break
    db["booked"].pop(i)
    return jsonify(db["booked"])

