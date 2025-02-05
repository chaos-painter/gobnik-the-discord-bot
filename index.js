import dotenv from 'dotenv';
dotenv.config();


import { Client, GatewayIntentBits } from 'discord.js';

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
    GatewayIntentBits.GuildMembers,
    GatewayIntentBits.DirectMessages,
  ],
});


let quotes = [
  "И неважно, сколько вокруг тебя будет союзников. Когда ты умираешь, ты всегда одинок.",
  "Умереть ради победы и рисковать жизнью ради неё же — совершенно разные вещи.",
  "Между небом и землёй лишь я достойный"
];

client.login(process.env.DISCORD_TOKEN);

client.on("ready", () => {
  console.log("The Bot is ready.")
});

client.on("messageCreate", async (message) => {
  console.log(message)
  message.content = message.content.toLowerCase()
  if (message.content === "эу годжо") {
    let index = Math.floor(Math.random() * quotes.length)
    let quote = quotes[index]
    message.reply(quote)
  }
});