# from telebot import types
# import requests
#
# lis_ccy = []
# a = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/").json()
# for i in a:
#     lis_ccy.append(i["Ccy"] +" → "+ i["CcyNm_EN"])
#
#
# dictionary_dic = {"happy": "счастливый", "perplexed": "озадаченный",
#                   "cat": "кошка", "harmony": "гармония",
#                   "run": "бегать", "deceive": "обманывать",
#                   "blue": "синий", "pen": "ручка",
#                   "mobile": "мобильные", "exacerbate": "обострять", "serendipity": "случайность",
#                   "ephemeral": "эфемерный",
#                   "cap": "кепка",
#                   "jump": "прыгать",
#                   "encounter": "сталкиваться",
#                   "benevolent": "доброжелательный",
#                   "laptop": "ноутбук", "picture": "картина", "maybe": "может быть", "car": "машина"}
#
# wikipedia_dic = {
#     "python": "Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. It has a large standard library and a vibrant community, making it suitable for various applications, from web development and data analysis to artificial intelligence and scientific computing.",
#     "java": "Java is a widely-used, object-oriented programming language developed by Sun Microsystems (now owned by Oracle Corporation) in the mid-1990s. It was designed to be platform-independent, meaning that Java programs can run on any device or operating system that has a Java Virtual Machine (JVM) installed. Java is known for its write once, run anywhere mantra, making it popular for building large-scale, enterprise-level applications, web applications, mobile apps (using Android), and more. It's also widely used in backend development, particularly in enterprise environments. Java's syntax is similar to C++, making it relatively easy for developers to transition to from other languages.",
#     "js": "JavaScript (JS) is a high-level, interpreted programming language primarily used for adding interactivity and dynamic behavior to web pages. It was created by Brendan Eich at Netscape in 1995 and has since become one of the most widely used programming languages. JavaScript allows developers to manipulate HTML and CSS, handle events, create animations, and interact with web browsers. It is commonly used in frontend web development, but with the advent of technologies like Node.js, it can also be used for server-side development. JavaScript is often used alongside HTML and CSS to create modern, interactive web applications.",
#     "c++": "C++ is a powerful, general-purpose programming language developed by Bjarne Stroustrup in the early 1980s. It is an extension of the C programming language with added features such as object-oriented programming (OOP) and generic programming. C++ is widely used for developing system software, game engines, desktop applications, embedded systems, and performance-critical applications. It provides a rich standard library and supports low-level programming, making it suitable for building efficient and scalable software. C++ is known for its performance and flexibility but can have a steeper learning curve compared to other languages due to its complexity.",
#     "c": "C is a powerful and widely used procedural programming language developed in the early 1970s by Dennis Ritchie at Bell Labs. It is known for its efficiency, flexibility, and portability, making it suitable for a wide range of applications, including system programming, embedded systems, and developing operating systems. C is often referred to as the mother of all programming languages due to its influence on the development of many other languages. It provides low-level access to memory, making it suitable for developing software where performance and control over hardware are critical. Despite being an older language, C remains popular and relevant today, particularly in fields where performance and efficiency are paramount.",
#     "assembly": "Assembly language, often referred to simply as assembly, is a low-level programming language that closely corresponds to machine code instructions for a specific computer architecture. Each assembly language instruction typically corresponds to a single machine instruction, making it a human-readable representation of machine code. Programmers use assembly language to write programs that directly control the computer's hardware at a low level. Assembly language is specific to the architecture of the target processor, meaning that programs written in assembly for one type of processor will not run on another type without modification. Despite its low-level nature and complexity, assembly language provides programmers with precise control over the hardware, allowing them to optimize code for performance-critical applications such as device drivers, real-time systems, and embedded systems. However, due to its complexity and architecture-specific nature, assembly language programming is less common than high-level programming languages in most modern software development scenarios.",
#     "go": "Go, also known as Golang, is a statically typed, compiled programming language developed by Google in 2007 and released to the public in 2009. It was designed with simplicity, efficiency, and concurrency in mind, aiming to provide a modern and productive language for building scalable and reliable software systems.Go features a clean and concise syntax, garbage collection, built-in support for concurrency through goroutines and channels, and a rich standard library. It is well-suited for developing web servers, network services, cloud-native applications, and distributed systems.Go's simplicity and performance make it popular among developers for a wide range of applications, from web development to system programming. Its concurrency primitives make it particularly well-suited for writing concurrent and parallel programs, allowing developers to efficiently utilize multicore processors and handle concurrent tasks easily.",
#     "ruby": "Ruby is a dynamic, object-oriented programming language with a focus on simplicity and productivity. It was designed by Yukihiro Matsumoto (Matz) in the mid-1990s and released to the public in 1995. Ruby emphasizes human-readable syntax and follows the principle of least surprise, aiming to make programming enjoyable and natural for developers.Key features of Ruby include:\n1. Object-oriented: Everything in Ruby is an object, including primitive data types. It supports classes, inheritance, and mixins.\n2. Dynamic typing: Ruby is dynamically typed, meaning that variable types are determined at runtime.\n3. Blocks and Procs: Ruby has first-class support for blocks, which are chunks of code that can be passed around like objects. Procs are Ruby's version of anonymous functions.\n4. Metaprogramming: Ruby allows for powerful metaprogramming techniques, enabling developers to write code that can modify itself at runtime.\n5. Rails: Ruby on Rails, often simply referred to as Rails, is a popular web application framework written in Ruby. It follows the convention over configuration (CoC) and don't repeat yourself (DRY) principles, allowing developers to build web applications quickly and efficiently.\nRuby's elegant syntax and focus on developer happiness have made it a favorite among web developers, particularly for building web applications and prototypes rapidly. However, its performance can be a concern for performance-critical applications, leading some developers to choose other languages for such use cases.",
#     "html": "HTML (Hypertext Markup Language) is the standard markup language used for creating web pages and web applications. It defines the structure and content of a webpage by using a system of tags and attributes. HTML documents consist of a series of elements, each represented by tags enclosed in angle brackets.Key features of HTML include:\n1. Tags: HTML documents are made up of tags, which define the structure and content of the page. Tags are enclosed in angle brackets (< >) and typically come in pairs, with an opening tag and a closing tag.\n2. Attributes: Tags can have attributes, which provide additional information about the element. Attributes are specified within the opening tag and typically consist of a name and a value.\n3. Structure: HTML documents have a hierarchical structure, with elements nested inside other elements to represent the layout and organization of content on the page.\n4. Semantics: HTML provides semantic elements that convey meaning about the content they contain, such as headings, paragraphs, lists, and tables. This helps improve accessibility and search engine optimization.\n5. Compatibility: HTML is supported by all modern web browsers and is compatible with various devices and platforms, making it suitable for creating cross-platform web content.\nHTML is often used in conjunction with CSS (Cascading Style Sheets) and JavaScript to create visually appealing and interactive web pages. CSS is used to style the appearance of HTML elements, while JavaScript is used to add interactivity and dynamic behavior to web pages.",
#     "css": "CSS (Cascading Style Sheets) is a style sheet language used to describe the presentation of a document written in HTML or XML. It controls the layout, appearance, and formatting of web pages, allowing developers to define styles such as colors, fonts, margins, and positioning.\nKey features of CSS include:\n1. Selectors: CSS selectors are patterns used to select and style HTML elements. They can target elements based on their tag name, class, ID, attributes, or relationship with other elements.\n2. Properties: CSS properties define the visual appearance of selected elements. Properties include attributes like color, font-size, width, height, margin, padding, background-color, and many others.\n3. Values: CSS properties are assigned values that specify how the selected elements should be styled. Values can be keywords, such as bold or italic, or numerical values, such as pixel measurements or percentages.\n4. Cascading: CSS follows a cascading mechanism, meaning that multiple style sheets can be applied to a single HTML document, and conflicting styles are resolved based on specificity and the order of precedence.\n5. Responsive design: CSS allows developers to create responsive layouts that adapt to different screen sizes and devices. Techniques like media queries and flexbox/grid layouts are commonly used to achieve responsive designs.\n6. Modularization: CSS can be organized into separate files and reused across multiple web pages, making it easier to maintain and update the styling of a website.\nCSS is an essential tool for web developers and designers, enabling them to create visually appealing and user-friendly web interfaces. It works seamlessly with HTML and JavaScript to enhance the presentation and functionality of web page\n"
# }
# dictionary_lis = [i for i in dictionary_dic.keys()]
# words = ""
# count = 1
# for i in dictionary_dic:
#     words += f"{count}. {i} \n"
#     count += 1
#
# amount = 1
# wikipedia = ""
# for i in wikipedia_dic.keys():
#     wikipedia += f"{amount}. {i} \n"
#     amount += 1
#
# quantity = 1
# lis_of_ccy = ""
# for i in lis_ccy:
#     lis_of_ccy += f"{quantity}. {i} \n"
#     quantity += 1
#
#
# def menu():
#     mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton("From ... to UZS")
#     button2 = types.KeyboardButton("Dictionary")
#     button3 = types.KeyboardButton("Wikipedia")
#     mark.add(button1, button2, button3)
#     return mark
#
#
# def rate(money, first, second):
#     a = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/" + first + "/").json()
#     total_sum = (f" 1 {first} = {a[0]["Rate"]} {second} \n"
#                  f" {money} {first} = {round(float(money * float(a[0]["Rate"])), 2)} {second}")
#
#     return total_sum
