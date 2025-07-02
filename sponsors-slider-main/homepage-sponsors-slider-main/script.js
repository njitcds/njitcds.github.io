window.addEventListener('load', function () {
  const slider = document.querySelector('.slider');
  const sliderWrapper = document.querySelector('.slider-wrapper');
  let style = sliderWrapper.querySelector('style');
  if (style == null) {
     console.log("adding style again");
     sliderWrapper.appendChild(document.createElement('style'));
     style = sliderWrapper.querySelector('style');
  }
  
  //function to create sliding effect
  function createDynamicKeyframes() {
    if (!(sliderWrapper.dataset.sliding === "true")) return;
    
    let slides =  Array.from(slider.getElementsByClassName("slide"));
    let slideStyle = window.getComputedStyle(slides[0]);
    let slideWidth = slides[0].offsetWidth + parseInt(slideStyle.marginLeft) + parseInt(slideStyle.marginRight);
    let sliderMinWidth = sliderWrapper.offsetWidth + slideWidth;
    slider.style.minWidth = `${sliderMinWidth}px`;
    slider.style.transform = `translateX(${-slideWidth}px)`;
    const sliderRect = slider.getBoundingClientRect();
    let sliderWidth = slider.offsetWidth;
    style.innerHTML = "";
    slides.forEach((slide, idx) => {
      let slideRect = slide.getBoundingClientRect();
      let total = sliderWidth;
      const relativeLeft = slideRect.left - sliderRect.left;
      let right = {
        shift: total - relativeLeft,
        percentage: (total - relativeLeft)*100/total,
      }
      const keyframes = `
        @keyframes slide${idx} {
          0% {
            transform: translateX(0);
          }
          ${right.percentage}% {
            transform: translateX(${right.shift}px);
          }
          ${right.percentage + 0.01}% {
            transform: translateX(${-relativeLeft}px);
          }
          100% {
            transform: translateX(0);     
          }
        }
      `;
      style.innerHTML += keyframes;
      slide.style.animation = `slide${idx} ${sliderWidth/slideWidth * 1}s linear infinite`;
    });
  }

  createDynamicKeyframes();

  window.addEventListener('resize', createDynamicKeyframes);
});
