let imagesItems = [...document.querySelectorAll(".img-wrap")]; //nodelistではなく、配列で取得できる
// console.log(imagesItems);
let titles = [...document.querySelectorAll("h2")];
let titleMessage = document.querySelector(".title");

//具体的にいつ発動させるのかを決めるオプション
let options = {
  rootMargin: "0px", //デフォルトで０.marginとほぼ同じ。
  threshold: 0.5, //閾値は0.2。これが１になると完全に画面におさまってから発動する
};

//ある特定の位置を超えると作動する関数
let setItemActive = (entries) => {
  console.log(entries);
  entries.map((entry) => {
    //mapは返り値を持つ（新しく配列を生成する）、forEachは返り値を持たない。
    // console.log(entry.isIntersecting);
    if (entry.isIntersecting) {
      entry.target.classList.add("active");
    } else {
      entry.target.classList.remove("active");
    }
  });
};

let observer = new IntersectionObserver(setItemActive, options); //交差の監視して、閾値を過ぎたらコールバック関数が呼ばれる

//img-wrapは偶数と奇数で出現する場所が違う。という処理。
imagesItems.map((item, index) => {
  console.log(item, index);
  //jsで楽にcssつけてるだけ。手動で１つずつつけても良い。でも要素名を変更するのが面倒臭いからこうしてる。
  item.children[0].style.backgroundImage = `url(./images/${index + 1}.jpg)`;
  index % 2 == 0 ? (item.style.left = "55%") : (item.style.left = "5%");
  //
  observer.observe(item); //itemを常に監視する。
});

titles.map((title, index) => {
  index % 2 == 0 ? (title.style.left = "45%") : (title.style.left = "35%");
  observer.observe(title);
});

observer.observe(titleMessage);