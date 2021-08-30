function navigationColor() {
  if (window.innerWidth >= 1280){
    let navigation = document.querySelector(".navigation").style.opacity = 0.8
  }
}

function navigationShift() {
  if (window.innerWidth >= 850) {
    let navigation = document.querySelector(".navigation")
    let state = false

    window.addEventListener("scroll", (e) => {
      let scrolled = window.scrollY

      if (scrolled >= 600 && state == false){
        console.log("Test1")
        // navigation.classList.toggle(".navigation-active")
        // navigation.classList.remove(".navigation")

        navigation.style.position = "fixed"
        navigation.style.opacity = 1

        state = true
      }

      else if (scrolled < 600 && state == true){
        console.log("Test2")
        // navigation.classList.toggle(".navigation-active")
        // navigation.classList.add(".navigation")

        navigation.style.position = "static"
        navigation.style.opacity = 0.8

        state = false
      }
    })
  }
}

function phoneNav() {
  let hamburger = document.querySelector(".hamburger")
  let dropdown = document.querySelector(".nav-dropdown")

  hamburger.addEventListener("click", (e) => {
    // dropdown.classList.toggle("nav-dropdown")
    dropdown.classList.toggle("nav-dropdown-active")
  })
}

phoneNav()
navigationShift()
navigationColor()