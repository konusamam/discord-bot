module.exports = (client, msg) => {
	// Ignore own messages unless Professional Rapper
	if (msg.author.id == client.user.id && msg.content.startsWith("```")) {
		if (msg.content.includes("❓ Right now?")) {
			let filter = reaction => reaction.emoji.name == "❓" || reaction.emoji.name == "👎"
			msg.awaitReactions(filter, {max: 1, time: 60000})
				.then(collected => {
					if (collected.first().emoji.name == "❓") {
						msg.channel.send(":man::skin-tone-2:: Right now?")
						msg.channel.send(":man::skin-tone-5:: Yeah")
						msg.channel.send("```md\n👍 Sure\n(react to this message)```")
					} else {
						msg.channel.send(`${collected.first().users.first()} Wrong answer, dog`)
					}
				})
				.catch(() => {
					msg.channel.send("Dog, why didn't you react? :(")
				})
		} else if (msg.content.includes("👍 Sure")) {
			let filter = reaction => reaction.emoji.name == "👍"
			msg.awaitReactions(filter, {max: 1, time: 60000})
				.then(collected => {
					if (collected.first().emoji.name == "👍") {
						msg.channel.send(":man::skin-tone-2:: Sure")
						msg.channel.send(":man::skin-tone-5:: Dope\n:man::skin-tone-5:: Juanita, bring some weed in here, please\n:man::skin-tone-5:: Thank you")
						msg.channel.send(":information_desk_person::skin-tone-5:‍: You got it, Snoop\n:information_desk_person::skin-tone-5:‍: I'll be right there")
						msg.channel.send("```md\n👏 Thanks, Juanita! (Super nice woman)\n(react to this message)```")
					}
				})
				.catch(() => {
					msg.channel.send("Dog, why didn't you react? :(")
				})
		} else if (msg.content.includes("👏 Thanks, Juanita! (Super nice woman)")) {
			let filter = reaction => reaction.emoji.name == "👏"
			msg.awaitReactions(filter, {max: 1, time: 60000})
				.then(collected => {
					if (collected.first().emoji.name == "👏") {
						msg.channel.send(":man::skin-tone-2:: Thanks, Juanita! (Super nice woman)")
						msg.channel.send(":man::skin-tone-5:: Diggo, why does everything you say sound so *soft*?")
						msg.channel.send("```md\n😠 Fuck you, diggo\n😞 Uh, I really don’t wanna be spoken to like that, so...\n(react to this message)```")
					}
				})
				.catch(() => {
					msg.channel.send("Dog, why didn't you react? :(")
				})
		} else if (msg.content.includes("😞 Uh, I really don’t wanna be spoken to like that, so...")) {
			let filter = reaction => reaction.emoji.name == "😞" || reaction.emoji.name == "😠"
			msg.awaitReactions(filter, {max: 1, time: 60000})
				.then(collected => {
					if (collected.first().emoji.name == "😞") {
						msg.channel.send(":man::skin-tone-2:: Uh, I really don’t wanna be spoken to like that, so...")
						msg.channel.send(":man::skin-tone-5:: Yeah, whatever")
						msg.channel.send(":information_desk_person::skin-tone-5:‍: Heyyyyy I got y'all your weed")
						msg.channel.send("```md\n🌿 Damn, that’s some great looking weed... it’s just so early...\n(react to this message)```")
					} else {
						msg.channel.send(`${collected.first().users.first()} Wrong answer, dog`)
					}
				})
				.catch(() => {
					msg.channel.send("Dog, why didn't you react? :(")
				})
		} else if (msg.content.includes("🌿 Damn, that’s some great looking weed... it’s just so early...")) {
			let filter = reaction => reaction.emoji.name == "🌿"
			msg.awaitReactions(filter, {max: 1, time: 60000})
				.then(collected => {
					if (collected.first().emoji.name == "🌿") {
						msg.channel.send(":man::skin-tone-2:: Damn, that’s some great looking weed... it’s just so early...")
						msg.channel.send(":information_desk_person::skin-tone-5:‍: Can I get you guys anything else while I’m here? Coffee? Tea? Head? Bottled water?")
						msg.channel.send("```md\n☕️ Coffee\n🍵 Tea\n❗ D-Did you just say head??\n💧 Water\n(react to this message)```")
					}
				})
				.catch(() => {
					msg.channel.send("Dog, why didn't you react? :(")
				})
		} else if (msg.content.includes("❗ D-Did you just say head??")) {
			let filter = reaction => reaction.emoji.name == "❗" || reaction.emoji.name == "☕" || reaction.emoji.name == "🍵" || reaction.emoji.name == "💧"
			msg.awaitReactions(filter, {max: 1, time: 60000})
				.then(collected => {
					if (collected.first().emoji.name == "❗") {
						msg.channel.send(":man::skin-tone-2:: D-Did you just say head??")
						msg.channel.send(":information_desk_person::skin-tone-5:‍: Yeah. You ain’t never got no head before?")
						msg.channel.send("```md\n🤔 I mean... just feels like... a lot... right now...\n😔 Nope\n(react to this message)```")
					} else {
						msg.channel.send(`${collected.first().users.first()} Wrong answer, dog`)
					}
				})
				.catch(() => {
					msg.channel.send("Dog, why didn't you react? :(")
				})
		} else if (msg.content.includes("🤔 I mean... just feels like... a lot... right now...")) {
			let filter = reaction => reaction.emoji.name == "🤔" || reaction.emoji.name == "😔"
			msg.awaitReactions(filter, {max: 1, time: 60000})
				.then(collected => {
					if (collected.first().emoji.name == "🤔") {
						msg.channel.send(":man::skin-tone-2:: I mean... just feels like... a lot... right now...")
						msg.channel.send(":information_desk_person::skin-tone-5:‍: ...OK")
						msg.channel.send("```md\n❓ But what kind of tea do you guys have?\n(react to this message)```")
					} else {
						msg.channel.send(`${collected.first().users.first()} Wrong answer, dog`)
					}
				})
				.catch(() => {
					msg.channel.send("Dog, why didn't you react? :(")
				})
		} else if (msg.content.includes("❓ But what kind of tea do you guys have?")) {
			let filter = reaction => reaction.emoji.name == "❓"
			msg.awaitReactions(filter, {max: 1, time: 60000})
				.then(collected => {
					if (collected.first().emoji.name == "❓") {
						msg.channel.send(":man::skin-tone-2:: But what kind of tea do you guys have?")
						msg.channel.send(":information_desk_person::skin-tone-5:‍: We got mint, raspberry, Earl Grey, English breakfast")
						msg.channel.send("```md\n🌱 Mint\n🍒 Raspberry \n🎩 Earl Grey\n🍴 English breakfast\n😏 Actually, I’ll take head\n(react to this message)```")
					}
				})
				.catch(() => {
					msg.channel.send("Dog, why didn't you react? :(")
				})
		} else if (msg.content.includes("😏 Actually, I’ll take head")) {
			let filter = reaction => reaction.emoji.name == "😏" || reaction.emoji.name == "🌱" || reaction.emoji.name == "🍒" || reaction.emoji.name == "🎩" || reaction.emoji.name == "🍴"
			msg.awaitReactions(filter, {max: 1, time: 60000})
				.then(collected => {
					if (collected.first().emoji.name == "😏") {
						msg.channel.send(":man::skin-tone-2:: Actually, I’ll take head")
						msg.channel.send(":no_good::skin-tone-5:‍: I knew yo dirty lil' ass wanted some head")
						msg.channel.send(`${collected.first().users.first()} You sly dog`)
					} else {
						msg.channel.send(`${collected.first().users.first()} Wrong answer, dog`)
					}
				})
				.catch(() => {
					msg.channel.send("Dog, why didn't you react? :(")
				})
		}
	} else if (msg.author.id == client.user.id) {
		return
	}

	let text = msg.content.toLowerCase()

	// Echo back -que messages. lmao
	if (text.endsWith("que")) {
		msg.channel.send(msg.content + " indeed.")
	}

	// Echo back -oo and -ical messages as well
	if (text.endsWith("oo") || text.endsWith("ical")) {
		msg.channel.send("Troogical")
	}

	// Prompt a command if only "doge"
	// if (text == "doge") {
	// 	let doge_reply = "Doge! "
	// 	let doge_emojis = ["🐶", "🐨", "🐼", "🦊", "🐻", "🦁", "🐮", "🐷", "🐸", "❤️", "💙", "💜", "💛", "💚", "💖"]
	// 	for (let i = 0; i < 5; i++) {
	// 		doge_reply += doge_emojis[Math.floor(Math.random() * doge_emojis.length)]
	// 	}
	// 	msg.channel.send(doge_reply)
	// 	msg.channel.send("Use **doge help** for a list of commands!")
	// }

	// Prompt a command if only "doge"
	if (text == "dogick") {
		let doge_reply = "Dogick! "
		let doge_emojis = ["🐶", "🐨", "🐼", "🦊", "🐻", "🦁", "🐮", "🐷", "🐸", "❤️", "💙", "💜", "💛", "💚", "💖"]
		for (let i = 0; i < 5; i++) {
			doge_reply += doge_emojis[Math.floor(Math.random() * doge_emojis.length)]
		}
		msg.channel.send(doge_reply)
	}

	// Ignore messages that don't start with doge (except for above cases)
	if (!text.startsWith("dogick ")) {
		if (text.includes("d0ge")) {
			msg.channel.send("I am **DOGICK**, you disgusting heathen.")
		} else if (text.includes("doge")) {
			msg.channel.send("I am **DOGICK**, you disgusting heathen.")
		}
		return
	}

	// Strip doge keyword from the rest of the command
	text = text.slice(7)

	if (text.startsWith("play ")) {
		text = text.slice(5)
		switch (text) {
		case "despacito":
			msg.channel.send("🎵DES🎵\n🎵PA🎵\n🎵DIGGO🎵\n🎵Quiero respirar tu cuello despadiggo🎵\n🎵Deja que te digga cosas al oído 🎵\n🎵Para que te acuerdes si no estás diggo 🎵")
			// Leaving this in for future reference
			//
			// let voiceChannel = msg.member.voiceChannel
			// voiceChannel.join().then(connection => {
			// 	const dispatcher = connection.playFile("./images/despacito.mp3")
			// 	dispatcher.on("end", end => {voiceChannel.leave()})
			// }).catch(err => console.log(err))
			break
		case "legends never die":
			msg.channel.send("🎵LEGENDS NEVER DIE🎵\n🎵THEY BECOME A PART OF YOU🎵\n🎵EVERY TIME YOU BLEED REACHING FOR GREATNESS🎵\n🎵LEGENDS NEVER DIE🎵")
			break
		case "professional rapper":
			msg.channel.send(":man::skin-tone-2:: 🎤I’m bout to be professional🎤\n:man::skin-tone-2:: 🎤Homie, I’m professional🎤")
			msg.channel.send(":man::skin-tone-5:: Whatever dog, you tryna smoke a blunt?")
			msg.channel.send("```md\n❓ Right now?\n👎 No thanks.\n(react to this message)```")
			break
		default:
			msg.channel.send("Roop, I couldn't find " + msg.content.slice(10) + " in my playlist. 😪")
			msg.channel.send("Here are the songs I know:")
			msg.channel.send("`Despacito`")
			msg.channel.send("`Legends Never Die`")
			msg.channel.send("`Professional Rapper`")
		}
	} else if (text == "help") {
		msg.channel.send("Woof woof! I'm a doge.")
		msg.channel.send("Here are the tricks I know:")
		msg.channel.send("`Play *song*:` plays a song from my playlist")
		msg.channel.send("`Edit:` edit my commands")
	} else if (text == "edit") {
		msg.channel.send({embed: {
			color: 3447003,
			title: "Edit my commands",
			url: "https://youtu.be/dQw4w9WgXcQ"
		}})
	} else if (text == "doggystyle") {
		msg.channel.send("OwO what's this? 😳❓Big red ❤💋meaty steak 🥩🍖 UwU ❤❤ 💖Mmm~ So tasty yummy UwO 😉😘, *licks meat*👅👅 💓💓Unnf UwU tastesss soo gwoood daddy ☺🤩😜~~ What?! ⁉️ EGGS?!?🥚⁉️ :0 😮 UwU *Shakeys wittle baby tail*🐶💖❤ mmm Daddy I Wuuuuv eggs~ 🥚💋💖I Wuuuuuuuv💗 💞 Yo Eggs espweciawy uwo, mmm tastes soooo good~ 💦🤤💙Daddy these eggs are sawty~💖💖 OwO ❤😍 daddy is that a sausage to add to my sawty eggy weggys?💖 🤤🥚💗 Mmm *licks sausage* 👅💦 mmmm soooo good~ 🤤💖🥴 *deepthroatys daddies big thick juicy meat* 😳👅 mmmm daddy this tastes SOOOOO GOOOOOD~ 😜💦💜MMMM OwO UwU~ *Nuzzles you*💗 RAWR 🐯🐻🦁💞")
	} else {
		msg.channel.send(`Roop, I didn't understand this command: **${msg.content.slice(5)}**`)
	}
}