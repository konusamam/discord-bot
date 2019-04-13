module.exports = (client, msg) => {
	
	if (msg.author.bot) {  // Ignore own messages
		return
	}

	let text = msg.content.toLowerCase()

	let dogical_words = ["d0g", "d0ge", "dogical", "dogger", "dorg", "dogue", "dorq"]
	for (let word of dogical_words) {
		if (text.includes(word)) {
			msg.channel.send("Doge!!🐕🐕🐕")
			return
		}
	}

	if (text.includes("doge")) {
		let num_doges = text.split("doge").length - 1
		let dogical_reply = "Doge"
		for (let i = 1; i < num_doges; i++) {
			dogical_reply += "doge"
		}
		dogical_reply += "!!!!!!!"
		let dogical_emojis = ["🐶", "🐨", "🐼", "🦊", "🐱", "❤️", "💙", "💜", "🧡", "💛", "💚", "💖"]
		for (let i = 0; i < (Math.floor(Math.random() * 12) + 5); i++) {
			dogical_reply += dogical_emojis[Math.floor(Math.random() * 12)]
		}
		msg.channel.send(dogical_reply)
	} else if (text == "dog") {
		msg.channel.send("I am no mere dog. I am DOGE.")
	} else if (text == "help") {
		msg.channel.send("woof woof! I'm a doge.")
	} else if (text == "doggystyle") {
		msg.channel.send("OwO what's this? 😳❓Big red ❤💋meaty steak 🥩🍖 UwU ❤❤ 💖Mmm~ So tasty yummy UwO 😉😘, *licks meat*👅👅 💓💓Unnf UwU tastesss soo gwoood daddy ☺🤩😜~~ What?! ⁉️ EGGS?!?🥚⁉️ :0 😮 UwU *Shakeys wittle baby tail*🐶💖❤ mmm Daddy I Wuuuuv eggs~ 🥚💋💖I Wuuuuuuuv💗 💞 Yo Eggs espweciawy uwo, mmm tastes soooo good~ 💦🤤💙Daddy these eggs are sawty~💖💖 OwO ❤😍 daddy is that a sausage to add to my sawty eggy weggys?💖 🤤🥚💗 Mmm *licks sausage* 👅💦 mmmm soooo good~ 🤤💖🥴 *deepthroatys daddies big thick juicy meat* 😳👅 mmmm daddy this tastes SOOOOO GOOOOOD~ 😜💦💜MMMM OwO UwU~ *Nuzzles you*💗 RAWR 🐯🐻🦁💞")
	} else if (text.includes("wtf")) {
		msg.channel.send("dooooooooooooooge", {
			file: "./images/doge.gif"
		})
	}
}
