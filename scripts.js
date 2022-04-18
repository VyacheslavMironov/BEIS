const navbar = document.querySelector(".navbar")
      allLi = document.querySelectorAll("li");

allLi.forEach((li, index)=> {
    li.addEventListener("click" , e =>{
        e.preventDefault(); //preventing from sumbitting
        navbar.querySelector(".active").classList.remove("active");
        li.classList.add("active");
        var indicator = document.querySelector(".indicator");
        indicator.style.transform = `translateX(calc(${index * 90}px))`;
    });
});