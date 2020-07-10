console.log("Connected!");
document.querySelector(".alert-danger").style.display="none";
document.querySelector(".alert-success").style.display="none";
var com=document.querySelector("#ms");
com.addEventListener("click",function(){
  document.querySelector(".alert-danger").style.display="none";
  document.querySelector(".alert-success").style.display="block";
  document.querySelector(".alert-success").textContent="Kindly enter the Relevant information";
});
var pas= document.querySelector("#ps");
pas.addEventListener("click",function(){
  document.querySelector(".alert-success").style.display="none";
  document.querySelector(".alert-danger").style.display="block";
  document.querySelector(".alert-danger").textContent="Password Protocol : A min. of 8 characters with atleast one number, one lower case and one upper case alphabet and a maximum of 16 characters";
});
var pasCheck = document.querySelector("#psc");
pasCheck.addEventListener("change",function(){
  console.log("1");
  if(pas.value!==pasCheck.value){
    $('#ps').addClass("turnrd");
    $('#psc').addClass("turnrd");
  }
  else{
    $('#ps').addClass("turngr");
    $('#psc').addClass("turngr");
  }
});
// var st=document.querySelector("#slc");
// var obj=document.querySelector("select");
// obj.addEventListener("click",function(){
//   st.disabled=true;
// })
var mails=document.querySelectorAll(".dropdown-item");
document.querySelector("#g").addEventListener("click",function(){
  var box = document.querySelector("#ms");
  var alr = box.value;
  box.value = alr+ "@gmail.com";
});
var mails=document.querySelectorAll(".dropdown-item");
document.querySelector("#y").addEventListener("click",function(){
  var box = document.querySelector("#ms");
  var alr=box.value;
  box.value=alr+"@yahoo.com";
});
var mails=document.querySelectorAll(".dropdown-item");
document.querySelector("#h").addEventListener("click",function(){
  var box = document.querySelector("#ms");
  var alr=box.value;
  box.value=alr+"@hotmail.com";
});
