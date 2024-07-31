
javascript:(function(){
  var s = document.createElement('style');
  s.innerHTML = `
:root {
  --max-translation: 0px;  /* pixels */
  --translation-phase: -3; /* radians */
  --max-skew: 18;          /* degrees */
  --max-scale-diff: 0.15;  /* scale factor */
  --anim-freq: 2;          /* Hz */

  --anim-time: calc(1/var(--anim-freq) * 1s);
}


.🦜 {
  animation: 🎉 var(--anim-time) infinite linear, 🎨 var(--anim-time) infinite linear;
  transform-origin: bottom center;
}

@keyframes 🎨 {
  0%,
  100% { background-color: #ff8d8b; }
  11.11% { background-color: #fed689; }
  22.22% { background-color: #88ff89; }
  33.33% { background-color: #87ffff; }
  44.44% { background-color: #8bb5fe; }
  55.56% { background-color: #d78cff; }
  66.67% { background-color: #ff8cff; }
  77.78% { background-color: #ff68f7; }
  88.89% { background-color: #fe6cb7; }
}

@keyframes 🎉 {
  0.0% {
    transform:
    skewX(calc(var(--max-skew) * -1.0000deg))
    translateX(calc(var(--max-translation) * sin(0.0000 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * 0.0000));
  }
  5.0% {
    transform:
    skewX(calc(var(--max-skew) * -0.9511deg))
    translateX(calc(var(--max-translation) * sin(0.3142 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * 0.3090));
  }
  10.0% {
    transform:
    skewX(calc(var(--max-skew) * -0.8090deg))
    translateX(calc(var(--max-translation) * sin(0.6283 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * 0.5878));
  }
  15.0% {
    transform:
    skewX(calc(var(--max-skew) * -0.5878deg))
    translateX(calc(var(--max-translation) * sin(0.9425 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * 0.8090));
  }
  20.0% {
    transform:
    skewX(calc(var(--max-skew) * -0.3090deg))
    translateX(calc(var(--max-translation) * sin(1.2566 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * 0.9511));
  }
  25.0% {
    transform:
    skewX(calc(var(--max-skew) * -0.0000deg))
    translateX(calc(var(--max-translation) * sin(1.5708 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * 1.0000));
  }
  30.0% {
    transform:
    skewX(calc(var(--max-skew) * 0.3090deg))
    translateX(calc(var(--max-translation) * sin(1.8850 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * 0.9511));
  }
  35.0% {
    transform:
    skewX(calc(var(--max-skew) * 0.5878deg))
    translateX(calc(var(--max-translation) * sin(2.1991 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * 0.8090));
  }
  40.0% {
    transform:
    skewX(calc(var(--max-skew) * 0.8090deg))
    translateX(calc(var(--max-translation) * sin(2.5133 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * 0.5878));
  }
  45.0% {
    transform:
    skewX(calc(var(--max-skew) * 0.9511deg))
    translateX(calc(var(--max-translation) * sin(2.8274 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * 0.3090));
  }
  50.0% {
    transform:
    skewX(calc(var(--max-skew) * 1.0000deg))
    translateX(calc(var(--max-translation) * sin(3.1416 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * 0.0000));
  }
  55.0% {
    transform:
    skewX(calc(var(--max-skew) * 0.9511deg))
    translateX(calc(var(--max-translation) * sin(3.4558 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * -0.3090));
  }
  60.0% {
    transform:
    skewX(calc(var(--max-skew) * 0.8090deg))
    translateX(calc(var(--max-translation) * sin(3.7699 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * -0.5878));
  }
  65.0% {
    transform:
    skewX(calc(var(--max-skew) * 0.5878deg))
    translateX(calc(var(--max-translation) * sin(4.0841 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * -0.8090));
  }
  70.0% {
    transform:
    skewX(calc(var(--max-skew) * 0.3090deg))
    translateX(calc(var(--max-translation) * sin(4.3982 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * -0.9511));
  }
  75.0% {
    transform:
    skewX(calc(var(--max-skew) * 0.0000deg))
    translateX(calc(var(--max-translation) * sin(4.7124 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * -1.0000));
  }
  80.0% {
    transform:
    skewX(calc(var(--max-skew) * -0.3090deg))
    translateX(calc(var(--max-translation) * sin(5.0265 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * -0.9511));
  }
  85.0% {
    transform:
    skewX(calc(var(--max-skew) * -0.5878deg))
    translateX(calc(var(--max-translation) * sin(5.3407 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * -0.8090));
  }
  90.0% {
    transform:
    skewX(calc(var(--max-skew) * -0.8090deg))
    translateX(calc(var(--max-translation) * sin(5.6549 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * -0.5878));
  }
  95.0% {
    transform:
    skewX(calc(var(--max-skew) * -0.9511deg))
    translateX(calc(var(--max-translation) * sin(5.9690 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * -0.3090));
  }
  100.0% {
    transform:
    skewX(calc(var(--max-skew) * -1.0000deg))
    translateX(calc(var(--max-translation) * sin(6.2832 + var(--translation-phase))))
    scaleY(calc(1 + var(--max-scale-diff) * -0.0000));
  }
}
  `;
  document.head.appendChild(s);
})();
