// Wrap every letter in a span
var textWrapper = document.querySelector(".ml11 .letters");
textWrapper.innerHTML = textWrapper.textContent.replace(/([^\x00-\x80]|\w)/g, "<span class='letter'>$&</span>");

anime
  .timeline({ loop: false })
  .add({
    targets: ".ml11 .line",
    scaleY: [0, 1],
    opacity: [0.5, 1],
    easing: "easeOutExpo",
    duration: 1000,
  })
  .add({
    targets: ".ml11 .line",
    translateX: [0, document.querySelector(".ml11 .letters").getBoundingClientRect().width + 10],
    easing: "easeOutExpo",
    duration: 700,
    delay: 100,
    opacity: 0,
  })
  .add({
    targets: ".ml11 .letter",
    opacity: [0, 1],
    easing: "easeOutExpo",
    duration: 900,
    offset: "-=775",
    delay: (el, i) => 34 * (i + 1),
  })
  .add({
    targets: ".ml11",
    duration: 1100,
    easing: "easeOutExpo",
    delay: 1000,
  });

//efek universitas
// Wrap every letter in a span
var textWrapper = document.querySelector(".ml12");
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime
  .timeline({ loop: true })
  .add({
    targets: ".ml12 .letter",
    translateX: [40, 0],
    translateZ: 0,
    opacity: [0, 1],
    easing: "easeOutExpo",
    duration: 1200,
    delay: (el, i) => 500 + 30 * i,
  })
  .add({
    targets: ".ml12 .letter",
    translateX: [0, -30],
    opacity: [1, 0],
    easing: "easeInExpo",
    duration: 1100,
    delay: (el, i) => 100 + 30 * i,
  });

// My Project

// // Wrap every letter in a span
// var textWrapper = document.querySelector(".ml9 .letters");
// textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

// anime
//   .timeline({ loop: true })
//   .add({
//     targets: ".ml9 .letter",
//     scale: [0, 1],
//     duration: 1500,
//     elasticity: 600,
//     delay: (el, i) => 45 * (i + 1),
//   })
//   .add({
//     targets: ".ml9",
//     opacity: 0,
//     duration: 1000,
//     easing: "easeOutExpo",
//     delay: 1000,
//   });
// // Akhir My Project

