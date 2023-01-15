let x = document.getElementById('container') ;
setInterval(func1 , 5000) ;
let bg = ['bg1.jpg','bg2.jpg','bg5.jpg','bg6.jpg'] ;

let va = 0 ;

        
function func1(){
        if(va == bg.length){
            va = 0;
        }
        x.style="background-image:url('/static/bg-images/{0}')".format(bg[va]);
        va+=1;


}
