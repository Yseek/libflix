/*!
* Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

const nonClick = document.querySelectorAll(".non-click");

function handleClick(event) {
  // div에서 모든 "click" 클래스 제거
nonClick.forEach((e) => {
    e.classList.remove("click");
});
  // 클릭한 div만 "click"클래스 추가
event.target.classList.add("click");
}

nonClick.forEach((e) => {
e.addEventListener("click", handleClick);
});

// 슬라이더
const next = document.querySelectorAll('.next');
const prev = document.querySelectorAll('.prev');
const slider = document.querySelectorAll('.slider')
for(let i =0;i<slider.length;i++){
    makeSlider(slider[i],prev[i],next[i]);
}
function makeSlider(element,prev,next){
    next.addEventListener('click',()=>{
        const offsetX = element.offsetWidth;
        element.scrollBy(offsetX,0)
    })
    prev.addEventListener('click',()=>{
        const offsetX = element.offsetWidth;
        element.scrollBy(-offsetX,0)
    })
}