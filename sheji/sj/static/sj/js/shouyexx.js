window.onload=function(){
    let circle=document.querySelectorAll('.circle')
    let box=document.querySelectorAll('.box')

    for(let i=0;i<circle.length;i++){
        circle[i].onclick=function(){
            for(let j=0;j<box.length;j++){
                box[j].style.zIndex=5
                circle[j].className='circle'
            }
            box[i].style.zIndex=10;
            circle[i].className='circle hot'
        }
    }
}