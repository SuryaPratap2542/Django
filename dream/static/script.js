const bar = document.getElementById("bar");
const close = document.getElementById("close");
const nav = document.getElementById("navbar");
if (bar){
    bar.addEventListener("click",() => {
        nav.classList.add('active');
    })
}

if (close){
    close.addEventListener("click",() => {
        nav.classList.remove('active');
    })
}
if (nav){
    window.addEventListener("scroll",()=>{
        nav.classList.remove("active")
    })
}
// const    navList = nav.querySelectorAll("li"),
//     totalNavList = navList.length,
//     allSection = document.querySelectorAll(".section"),
//     totalSection = allSection.length;

// for (let i = 0; i < totalNavList; i++) {

//     const a = navList[i].querySelector("a");
//     a.addEventListener("click", function () {
       
//         removeBackSection();
//         for (let j = 0; j < totalNavList; j++) {
//             if (navList[j].querySelector("a").classList.contains("active")) {
//                 // console.log("back-section"+ navList[j].querySelector("a"))
//                 addBackSection(j);
//                 // allSection[j].classList.add("back-section");
//             }
//             navList[j].querySelector("a").classList.remove("active");
//         }
//         this.classList.add("active")
//         showSection(this);
//         if(window.innerWidth<1200)
//         {
//             asideSectionTogglerBtn();
//         }
//     })
// }
// Toggle Style Switcher
// const styleSwitcherToggle= document.querySelector("#bar");
// styleSwitcherToggle.addEventListener("click",()=>{
//     document.querySelector("#mobile").classList.toggle("open");
// })

// hide style Switcher on scroll
// window.addEventListener("scroll",()=>{
//     console.log("scrolled");
//     if (document.querySelector(".mob").classList.contains("active"))
//     {
//         document.querySelector(".mob").classList.remove("open");
//     }
// })