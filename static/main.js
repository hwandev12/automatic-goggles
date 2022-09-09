console.log("Hello world")

// all stars here
const one = document.getElementById("first")
const two = document.getElementById("second")
const three = document.getElementById("third")
const four = document.getElementById("fourth")
const five = document.getElementById("fifth")

const form = document.querySelector(".rate-form")
const confirmBox = document.getElementById("confirm-box")

const csrf = document.getElementsByName("csrfmiddlewaretoken")

const handleChoose = (index) => {
	const children = form.children
	for (let i = 0; i < children.length; i++) {
		if( i <= index) {
			children[i].classList.add("checked")
		} else {
			children[i].classList.remove("checked")
		}
	}
}



const checkTrue = (selection) => {
	switch(selection){
		case "first": {
			// one.classList.add("checked")
			// two.classList.remove("checked")
			// three.classList.remove("checked")
			// four.classList.remove("checked")
			// five.classList.remove("checked")
			handleChoose(1)
			return
		}
		case "second": {
			handleChoose(2)
			return
		}
		case "third": {
			handleChoose(3)
			return
		}
		case "fourth": {
			handleChoose(4)
			return
		}
		case "fifth": {
			handleChoose(5)
			return
		}
	}
}


const items = [one, two, three, four, five]

items.forEach( item => item.addEventListener("mouseover", (event) => {
	checkTrue(event.target.id)
}))