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
