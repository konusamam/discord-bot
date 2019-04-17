module.exports = (client, msg) => {
	if (msg.author.bot) {  // Ignore own messages
		return
	}

	let text = msg.content.toLowerCase()

	if (text.includes("doge")) {
		let doge_reply = "Doge"
		let doge_emojis = ["🐶", "🐨", "🐼", "🦊", "🐻", "🦁", "🐮", "🐷", "🐸", "❤️", "💙", "💜", "💛", "💚", "💖"]
		let num_doges = text.split("doge").length - 1
		
		for (let i = 1; i < num_doges; i++) {
			doge_reply += "doge"
		}
		doge_reply += "!!!!!!!"

		for (let i = 0; i < (Math.floor(Math.random() * 12) + 5); i++) {
			doge_reply += doge_emojis[Math.floor(Math.random() * doge_emojis.length)]
		}

		msg.channel.send(doge_reply)
	} else if (text == "dog") {
		msg.channel.send("I am no mere dog. I am DOGE.")
	} else if (text.includes("d0g") || text.includes("d0ge")) {
		msg.channel.send("Doge!!🐕🐕🐕")
	} else if (text == "help") {
		msg.channel.send("woof woof! I'm a doge.")
	} else if (text.includes("dogical")) {
		msg.channel.send("Troogical")
	} else if (text.includes("troo")) {
		msg.channel.send("Trooby dooby doooooooooooooooooooooooooooooooooooooooooooo")
	} else if (text.includes("tarnation")) {
		msg.channel.send("Wot in perfidious albion")
	} else if (text.includes("que")) {
		msg.channel.send(msg.content + "indeed.")
	} else if (text.includes("rip") || text.includes("rop") || text.includes("roop")) {
		msg.channel.send("Press W to pay Woofspects", {
			file: "./images/doge.jpg"
		})
	} else if (text == "w") {
		msg.channel.send("```So we beat on,\nboats against the current,\nborne back ceaselessly into the past.```", {
			file: "./images/wol.jpg"
		})
	} else if (text.includes("what")) {
		msg.channel.send("What's this? UwU", {
			file: "./images/doge.gif"
		})
	} else if (text.includes("wot")) {
		msg.channel.send("Wot's this? UwU", {
			file: "./images/doge.gif"
		})
	} else if (text.includes("w0t")) {
		msg.channel.send("W0t's this? UwU", {
			file: "./images/doge.gif"
		})
	} else if (text.includes("nani")) {
		msg.channel.send("🅱️ani")
	} else if (text.includes("wait")) {
		msg.channel.send("Wait wot")
	} else if (text == "doggystyle") {
		msg.channel.send("OwO what's this? 😳❓Big red ❤💋meaty steak 🥩🍖 UwU ❤❤ 💖Mmm~ So tasty yummy UwO 😉😘, *licks meat*👅👅 💓💓Unnf UwU tastesss soo gwoood daddy ☺🤩😜~~ What?! ⁉️ EGGS?!?🥚⁉️ :0 😮 UwU *Shakeys wittle baby tail*🐶💖❤ mmm Daddy I Wuuuuv eggs~ 🥚💋💖I Wuuuuuuuv💗 💞 Yo Eggs espweciawy uwo, mmm tastes soooo good~ 💦🤤💙Daddy these eggs are sawty~💖💖 OwO ❤😍 daddy is that a sausage to add to my sawty eggy weggys?💖 🤤🥚💗 Mmm *licks sausage* 👅💦 mmmm soooo good~ 🤤💖🥴 *deepthroatys daddies big thick juicy meat* 😳👅 mmmm daddy this tastes SOOOOO GOOOOOD~ 😜💦💜MMMM OwO UwU~ *Nuzzles you*💗 RAWR 🐯🐻🦁💞")
	}
}
