console.log('product-view');

const list_of_imgs = document.querySelector('.list-of-imgs');
const images = list_of_imgs.getElementsByClassName('image');
var main_img=document.getElementById('main-img')

for (var i = 0; i < images.length; i++) {
    var img = images[i]
    img.addEventListener('click', (el) => {
        var img_src=el.target.src
        main_img.setAttribute('src',img_src)
        console.log(img_src)
    })
}