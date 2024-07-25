function showSidebar(){
    const sidebar = document.querySelector('.sidebar')

    sidebar.style.display = 'flex'

}


function hideSidebar(){
    const sidebar = document.querySelector('.sidebar')

    sidebar.style.display = 'none'
}











function spark(event){
    let i = document.createElement('i');
    i.style.left = (event.pageX) + 'px';
    i.style.top = (event.pageY) + 'px';
    i.style.scale = `${Math.random() * 2 + 1}`;
    i.style.setProperty('--x', getRandomTransitionValue());
    i.style.setProperty('--y', getRandomTransitionValue());
    document.body.appendChild(i);
    setTimeout(() => {
        document.body.removeChild(i);
    }, 2000)
}

function getRandomTransitionValue(){
    return `${Math.random() * 201 - 200}px`;
}

document.addEventListener('mousemove', spark);
