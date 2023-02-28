$(function(){
  $('.list').slick({
    slide: 'figure',        //슬라이드 되어야 할 태그
    infinite : false,     //무한 반복 옵션     
    slidesToShow : 6,        // 한 화면에 보여질 컨텐츠 개수
    slidesToScroll : 1,        //스크롤 한번에 움직일 컨텐츠 개수
    // speed : 500,     // 다음 버튼 누르고 다음 화면 뜨는데까지 걸리는 시간(ms)
    arrows : true,         // 옆으로 이동하는 화살표 표시 여부
    dots : false,         // 스크롤바 아래 점으로 페이지네이션 여부
    // autoplay : true,            // 자동 스크롤 사용 여부
    // autoplaySpeed : 2000,         // 자동 스크롤 시 다음으로 넘어가는데 걸리는 시간 (ms)
    pauseOnHover : true,        // 슬라이드 이동    시 마우스 호버하면 슬라이더 멈추게 설정
    vertical : false,        // 세로 방향 슬라이드 옵션
    prevArrow : "<button type='button' class='slick-prev'>Previous</button>",
    nextArrow : "<button type='button' class='slick-next'>Next</button>",
    draggable : true,     //드래그 가능 여부 
    responsive: [ // 반응형 웹 구현 옵션
      {  
        breakpoint: 960, //화면 사이즈 960px
        settings: {
          slidesToShow: 4
        } 
      },
      { 
        breakpoint: 768, //화면 사이즈 768px
        settings: {    
          slidesToShow: 5
        } 
      }
    ]

  });
})

document.querySelectorAll('.input1').forEach(e =>{
    document.getElementsByClassName("btn btn-outline-dark mt-auto1")[e.id].onclick = user_check;
    function user_check(){
        if(("{{request.session.login_}}").length==0){
            location.href="top_login__";
        }else{
            document.getElementsByClassName("form_cls1")[e.id].submit();
        }
    }
})
document.querySelectorAll('.input2').forEach(e =>{
    document.getElementsByClassName("btn btn-outline-dark mt-auto2")[e.id].onclick = user_check;
    function user_check(){
        if(("{{request.session.login_}}").length==0){
            location.href="top_login__";
        }else{
            document.getElementsByClassName("form_cls2")[e.id].submit();
        }
    }
})
document.querySelectorAll('.input3').forEach(e =>{
    document.getElementsByClassName("btn btn-outline-dark mt-auto3")[e.id].onclick = user_check;
    function user_check(){
        if(("{{request.session.login_}}").length==0){
            location.href="top_login__";
        }else{
            document.getElementsByClassName("form_cls3")[e.id].submit();
        }
    }
})
document.querySelectorAll('.input4').forEach(e =>{
    document.getElementsByClassName("btn btn-outline-dark mt-auto4")[e.id].onclick = user_check;
    function user_check(){
        if(("{{request.session.login_}}").length==0){
            location.href="top_login__";
        }else{
            document.getElementsByClassName("form_cls4")[e.id].submit();
        }
    }
})
document.querySelectorAll('.input5').forEach(e =>{
    document.getElementsByClassName("btn btn-outline-dark mt-auto5")[e.id].onclick = user_check;
    function user_check(){
        if(("{{request.session.login_}}").length==0){
            location.href="top_login__";
        }else{
            document.getElementsByClassName("form_cls5")[e.id].submit();
        }
    }
})
document.querySelectorAll('.input6').forEach(e =>{
    document.getElementsByClassName("btn btn-outline-dark mt-auto6")[e.id].onclick = user_check;
    function user_check(){
        if(("{{request.session.login_}}").length==0){
            location.href="top_login__";
        }else{
            document.getElementsByClassName("form_cls6")[e.id].submit();
        }
    }
})