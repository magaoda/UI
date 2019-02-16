window.onload=function(){
    let shouye=document.querySelector('.shouye')
    let qidong=document.querySelector('.qidong')
    let quesheng=document.querySelector('.quesheng')
    let box=document.querySelectorAll('.box')
    let circle=document.querySelectorAll('.circle')
  function move(){
    qidong.onclick=function(){
        qidong.style.display='none'
        quesheng.style.display='block'
    }

	for(let i=0;i<circle.length;i++){
	    circle[i].onclick=function(){
	        for(let j=0;j<box.length;j++){
	            box[j].style.zIndex=5
                circle[j].className='circle'
            }
	        box[i].style.zIndex=10;
            circle[i].className='circle hot'
        }

            // if (i==circle.length-1){
            //     box[i].onclick=function(){
            //         location.href="{% url 'sj:xuanze' %}"
            //     }
            // }
        }

    }
    setTimeout(move,1000)
}



