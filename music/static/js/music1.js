let x = document.getElementById('container') ;

let bg = ['bg1.jpg','bg2.jpg','bg5.jpg','bg6.jpg'] ;

var va = 0 ;

let u = document.createElement('style');
document.head.appendChild(u);

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
 }

async function bgi(va ,bg){
    await sleep(3000);
    if(va == bg.length){
        u.innerHTML = `#container{background-img:url('/static/bg-images/${bg[va]}')}`;
        
    
        va = 0 ;
    }
    else{
        u.innerHTML = `#container{background-img:url('/static/bg-images/${bg[va]}')}`;
        va = va + 1 
    }

}
bgi(0 , bg) ;