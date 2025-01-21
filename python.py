<!DOCTYPE html>
<html lang="en">
<head>
     
    <title>Homepage</title>
    <style>
        header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: rgb(107, 58, 2);
            z-index: 100;
        }
        html {
            scroll-behavior: smooth;
        }
        body {
            background: #fff;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        .flex {
            display: flex;
            align-items: center;
        }
        .container {
            max-width: 1200px;
            width: 100%;
            margin: 0 auto;
            padding: 0 20px;
        }
        .navbar {
            width: 100%;
            justify-content: space-between;
        }
        .nav-links {
            list-style: none;
            display: flex;
            gap: 20px;
            padding: 0;
        }
        .navbar a {
            padding: 20px 0;
            display: inline-block;
            color: white;
            text-decoration: none;
            text-transform: capitalize;
            transition: 0.2s;
        }
        .navbar a:hover {
            color: #ddd;
        }
        .homepage {
            position: relative;
            height: 100vh;
            display: flex;
            width: 100%;
            background: url("gemlib.png") no-repeat center/cover;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        .homepage::before {
            content: "";
            position: absolute;
            height: 100%;
            width: 100%;
            top: 0;
            left: 0;
            background: rgba(0, 0, 0, 0.2);
        }
        .homepage .content {
            position: relative;
            height: 85%;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .homepage .text {
            color: white;
            margin-bottom: 50px;
        }
        .homepage .text h1 {
            font-size: 60px;
            font-weight:normal;
            margin-bottom: 10px;
        }
        .homepage a {
            color: white;
            text-decoration: none;
            background: rgb(190, 94, 4);
            padding: 10px 30px;
            border-radius: 5px;
            border: 2px solid rgb(190, 94, 4);
            box-shadow: rgba(0, 0, 0, 0.3);
            font-size: 18px;
            transition: 0.3s;
        }
        .homepage a:hover {
            color: white;
            background: rgba(156, 79, 6, 0.541);
        }
        section {
            padding-top: 80px;
        }
        .section-title {
            text-align: center;
        }
        section h2 {
            font-size: 2rem;
        }
        section .cards {
            margin-top: 50px;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }
        section .card {
            width: calc(100% / 3 - 30px);
            text-align: center;
            list-style: none;
            background-color: rgb(231, 226, 155);
            padding: 40px 15px;
            border-radius: 5px;
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        section .card img {
            height: 120px;
            width: 120px;
            border-radius: 50%;
            margin-bottom: 20px;
        }
        section .card p {
            margin-top: 5px;
        }
        .portfolio .card {
            padding: 0 0 20px;
        }
        .portfolio .card img {
            height: 240px;
            width: 100%;
            border-radius: 8px 8px 0 0;
        }
        .about .company-info {
            margin-top: 30px;
        }
        .about .row {
            padding: 0 10px;
        }
        .about h3 {
            margin: 30px 0 10px;
        }
        .about ul {
            padding-left: 20px;
        }
        .contact .row {
            margin: 60px 0 90px;
            display: flex;
            justify-content: space-between;
        }
        .contact .row .col {
            padding: 0 10px;
            width: calc(100% / 2 - 50px);
        }
        .contact .row .col p {
            color: #423f3f;
            margin-bottom: 10px;
        }
        .contact .row .col p i {
            margin-right: 10px;
        }
        .contact form input,
        .contact form textarea {
            width: 100%;
            margin-bottom: 20px;
            padding: 15px;
            border: 1px solid #bfbfbf;
            outline: none;
        }
        .contact form button {
            padding: 10px 20px;
            border-radius: 6px;
            font-size: 17px;
            color: rgb(219, 219, 219);
            margin-top: 10px;
            border: none;
            background: rgb(107, 58, 2);
            transition: 0.2s;
            cursor: pointer;
        }
        .contact form button:hover {
            background: darkkhaki;
        }
        .footer {
            background: rgb(156, 78, 6);
            padding: 20px 0;
        }
        .footer span {
            color: white;
        }
        /*Responsive*/
        @media (width < 860px) {
        .navbar .nav-links {
            position: fixed;
            left: 0;
            top: 65px;
            height: 100%;
            display: block;
            background: rgb(107, 58, 2);
            width: 300px;
            padding-left: 20px;
            padding-top: 30px;
            left: -100%;
            transition: all 0.4s ease;
        }
        #menu-toggler:checked ~ .nav-links {
            left: 0;
        }
        .nav-links li {
            font-size: 18px;
        } @media (max-width: 600px) {
            #hamburger-btn {
            display: block;
            position: absolute;
            right: 20px;
            color: #fff;
            font-size: 22px;
            cursor: pointer;
        }
        .nav-links {
            display: none;
        }
        }
        @media (width>601px) { 
            #hamburger-btn, #menu-toggler {
                display:none ; 
            }
        }
        section .cards .card {
            width: calc(100% / 2 - 15px);
        }
        .contact .row {
            flex-direction: column;
        }
        .contact .row .col {
            width: 100%;
        }
        .contact .row .col:last-child {
            margin-top: 40px;
        }
    }

    @media (width < 560px) {
        section .cards .card {
            width: 100%;
        }
        .homepage .text h1 {
            font-size: 30px ;
        }
        section h2 {
            font-size: 1.5rem;
        }
    }
    </style>
</head>
<body>
    <header>
        <nav class="navbar container flex">
            <h2 class="logo"><a href="#"> LOGO </a></h2>
            <input type="checkbox" id="menu-toggler">
            <label for="menu-toggler" id="hamburger-btn">
                <i class="fa-solid fa-bars"></i>
            </label>
            <ul class="nav-links flex">
                <li><a href="#home">home</a></li>
                <li><a href="#services">services</a></li>
                <li><a href="#about">about us</a></li>
                <li><a href="#portfolio">portfolio</a></li> 
                <li><a href="#contact">contact us</a></li>
            </ul>
        </nav>
    </header>
    <section class="homepage" id="home">
        <div class="content flex">
            <div class="text">
                <h1>Library Management System</h1>
                <p>This is the first paragraph</p>
            </div>
            <a href="#services">Our services</a>
        </div>
    </section>
    <section class="services" id="services">
        <div class="container">
            <div class="section-title">
                <h2>Our Services</h2>
                <p>This is second paragraph</p>
            </div>
            <ul class="cards flex">
                <li class="card">
                    <img src="mathlogo.webp" alt="">
                    <h3>Mathematics</h3>
                    <p>This is for mathematics books</p>
                </li>
                <li class="card">
                    <img src="science logo.webp" alt="">
                    <h3>Science</h3>
                    <p>This is for science books</p>
                </li>
                <li class="card">
                    <img src="mathlogo.webp" alt="">
                    <h3>Computer</h3>
                    <p>This is for computer books</p>
                </li>
                <li class="card">
                    <img src="mathlogo.webp" alt="">
                    <h3>Social Sciences</h3>
                    <p>This is for social science books</p>
                </li>
                <li class="card">
                    <img src="mathlogo.webp" alt="">
                    <h3>Humanities</h3>
                    <p>This is for Humanities books</p>
                </li>
                <li class="card">
                    <img src="mathlogo.webp" alt="">
                    <h3>Commerce</h3>
                    <p>This is for Commerce books</p>
                </li>
                <li class="card">
                    <img src="mathlogo.webp" alt="">
                    <h3>Tragedy</h3>
                    <p>This is for Tragedy books</p>
                </li>
                <li class="card">
                    <img src="mathlogo.webp" alt="">
                    <h3>Comedy</h4>
                    <p>This is for Comedy books</p>
                </li>
                <li class="card">
                    <img src="mathlogo.webp" alt="">
                    <h3>Thriller</h3>
                    <p>This is for Thriller books</p>
                </li>
                <li class="card">
                    <img src="mathlogo.webp" alt="">
                    <h3>Horror</h3>
                    <p>This is for Horror books</p>
                </li>
                <li class="card">
                    <img src="mathlogo.webp" alt="">
                    <h3>Romance</h3>
                    <p>This is for Romance books</p>
                </li>
                <li class="card">
                    <img src="mathlogo.webp" alt="">
                    <h3>Biographies</h3>
                    <p>This is for Biography books</p>
                </li>
            </ul>
        </div>
    </section>
    <section class="portfolio" id="portfolio">
        <div class="container">
            <div class="section-title">
                <h2>Our Portfolio</h2>
                <p>This is the portfolio section</p>
            </div>
            <ul class="cards flex">
                <li class="card">
                    <img src="ferrari logo.jpeg" alt="">
                    <h3>portfolio</h3>
                    <p>This is for portfolio</p>
                </li>
                <li class="card">
                    <img src="ferrari logo.jpeg" alt="">
                    <h3>portfolio</h3>
                    <p>This is for portfolio</p>
                </li>
                <li class="card">
                    <img src="ferrari logo.jpeg" alt="">
                    <h3>portfolio</h3>
                    <p>This is for portfolio</p>
                </li>
            </ul>
        </div>
    </section>
    <section class="about" id="about">
        <div class="container">
            <div class="section-title">
                <h2>About Us</h2>
                <p>This is for about us section</p>
            </div>
            <div class="row company-info">
                <h3>Our Story</h3>
                <p>This is to write the history of creators of website</p>
                <h3>Our Vision</h3>
                <p>To become the leading online library management solution, empowering libraries worldwide to improve access to information, enhance literacy, and foster lifelong learning within their communities</p>
                <h3>Our Mission</h3>
                <p>To continuously innovate and improve library services by developing a cutting-edge online platform that leverages technology to streamline workflows, enhance accessibility, and foster a love of learning</p>
            </div>
            <div class="row team">
                <h3>Our Team</h3>
                <ul>
                    <li>Aritrika Dhara - Founder</li>
                </ul>
            </div>
        </div>
    </section>
    <section class="contact" id="contact">
        <div class="container">
            <div class="section-title">
                <h2>Contact Us</h2>
                <p>This is for contact us details</p>
            </div>
        </div>
        <div class="row flex">
            <div class="col information">
                <div class="contact-details">
                    <p><i class="fa-solid fa-location-dot"></i>Kamal Apartment, BD-203, Flat no-F2, Kamal Park, Kestopur, Kolkata-700101</p>
                    <p><i class="fa-solid fa-envelope"></i>aritrikadhara@gmail.com</p>
                    <p><i class="fa-solid fa-phone"></i>9331939960</p>
                    <p><i class="fa-solid fa-clock"></i>Monday - Friday : 9:00 am - 5:00 pm</p>
                    <p><i class="fa-solid fa-clock"></i>Saturday : 10:00 am - 4:00 pm</p>
                    <p><i class="fa-solid fa-clock"></i>Sunday : Closed</p>
                    <p><i class="fa-solid fa-globe"></i>www.librarymanagement.com</p>
                </div>
            </div>
            <div class="col form">
                <form action="#">
                    <input type="text" placeholder="Name*" required>
                    <input type="email" placeholder="Email*" required>
                    <textarea placeholder="Message*" required></textarea>
                    <button id="submit" type="submit">Send Message</button>
                </form>
            </div>
        </div>
    </section>
    <footer class="footer">
        <div class="container">
            <span>Copyright © 2024 All rights Reserved Home Contact</span>
        </div>
    </footer>

    <!-- FontAwesome script -->
    <script src="https://kit.fontawesome.com/e895b878fe.js" crossorigin="anonymous"></script>
</body>
</html>
