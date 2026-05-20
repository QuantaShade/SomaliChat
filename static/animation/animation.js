const modal = document.getElementById("form")
const openBtn = document.getElementById("openBtn")
const closeBtn = document.getElementById("closeBtn")

modal.style.scale = "0"

openBtn.addEventListener("click", () => {
    modal.style.scale = "1"
})

closeBtn.addEventListener("click", () => {
    modal.style.scale = "0"
})