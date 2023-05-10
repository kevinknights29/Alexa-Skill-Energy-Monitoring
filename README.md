# Alexa Skill

## Design with four critical goals in mind

---

As you design your skill, there are four core questions to the customer experience that you need to address:

<ol>
    <li>
        What’s the goal or purpose of your skill?
    </li>
    <p>
        Ans: Provide details about energy consumption and posible recomendations to reduce energy consumption
    </p>
    <li>
        How will customers invoke your skill?
    </li>
    <p>
        Ans: 
        <ul>
            <li>
                Alexa, how much is my energy consumption today?
            </li>
            <li>
                Alexa, how can I reduce my energy consumption?
            </li>
        </ul>
    </p>
    <li>
        What can a customer do with your skill?
    </li>
        <p>
            Ans:
            <ul>
                <li>
                    Identify energy consumption patterns
                </li>
                <li>
                    Create rules to optimize their energy consumption
                </li>
            </ul>
        </p>
    <li>
        What kinds of information do you need to collect from customers to personalize the experience?
    </li>
    </p>
        Ans: Devices connect to Alexa, their energy consumption and electric values.
    </p>
</ol>

<br>

## Invocation Name

---

### Invoke a skill with a specific request (intent)

Users can combine your invocation name with an action, command or question. This sends the service for your skill an IntentRequest with the specific intent that corresponds to the user's request. The action, command, or question included in the phrase comes from the sample utterances you define and map to intents.

Examples:

<ul>
    <li>EN-US:</li>
    <p><i>Alexa, ask <b>energy monitor</b> about how much electricity I consumed today.</i></p>
    <li>ES-MX:</li>
    <p><i>Alexa, preguntale a <b>monitor energetico</b> sobre cuanta energia electrica consumi hoy.</i></p>
    <p><i>Alexa, lanza <b>monitor energetico</b> para decirme cuanta energia electrica consumi hoy.</i></p>
    <p><i>Alexa, usa <b>monitor energetico</b> y dime cuanta energia electrica consumi hoy.</i></p>
    <p><i>Alexa, usa <b>monitor energetico</b> y dime que dispositivo consumio mas energia durante la semana.</i></p>
</ul>

<br>

### Invoke a skill with no specific request (no intent)

---

Users can begin interacting with your skill without providing a specific question, request, or command. This sends the service for your skill a LaunchRequest.

At a minimum, users can just say the wake word ("Alexa") and your skill's invocation name.

Examples:

<ul>
    <li>EN-US:</li>
    <p><i>Alexa, <b>energy monitor</b>.</i></p>
    <p><i>Alexa, ask <b>energy monitor</b>.</i></p>
    <p><i>Alexa, run <b>energy monitor</b>.</i></p>
    <li>ES-MX:</li>
    <p><i>Alexa, <b>monitor energetico</b>.</i></p>
    <p><i>Alexa, lanza <b>monitor energetico</b>.</i></p>
    <p><i>Alexa, usa <b>monitor energetico</b>.</i></p>
</ul>

<br>

### Make sure that the sample utterances support the invocation phrases

---

All of the phrases described in this document are available for all skills. You do not need to enable the specific phrases. However, you do need to write sample utterances that flow naturally with these phrases.

For example, if all of your sample utterances are phrased as questions ("what is the horoscope for Taurus"), then phrases that work with noun or verb utterances won't flow naturally. Users are unlikely to say something like "tell Daily Horoscopes what is the horoscope for Taurus," as this is not a natural way to ask this question. This reduces the number of useful invocation phrases.

For a better user experience, provide a large variety of sample utterances written in different forms:

Noun utterances ("the horoscope for…")
Verb utterances ("give me the horoscope for…")
Question utterances ("what is the horoscope for…")

<br>

### Invocation Name Requirements

---

An invocation name must meet the following requirements:

<ol>
<li>
The skill invocation name must not infringe upon the intellectual property rights of an entity or person. For more information about intellectual property policies, see Policy Testing for an Alexa Skill.
</li>

<li>
One-word invocation names are not allowed, unless:
The invocation name is unique to your brand/intellectual property with proof of ownership established through legitimate documentation, or
(German skills only) The invocation name is a compound of two or more words. In this case, the word must form an actual word in the skill's language to ensure that Alexa can recognize it.
For more information about intellectual property policies, see Policy Testing for an Alexa Skill.
</li>

<li>
Invocation names that include names of people or places (for example, "molly", "seattle") are not allowed, unless they contain other words (for example, "molly's horoscope," "seattle spotlight," "sam's market").
</li>

<li>
Two-word invocation names are not allowed if one of the words is a definite article ("the"), indefinite article ("a", "an") or preposition ("for", "to", "of," "about," "up," "by," "at," "off," "with"). For example, "a bicycle", "an espresso", "to amuse", "for fun".
</li>

<li>
The invocation name must not contain any of the Alexa skill launch phrases and connecting words.
Launch phrases include "run," "start," "play," "resume," "use," "launch," "ask," "open," "tell," "load," "begin," and "enable."
Connecting words include "to," "from," "in," "using," "with," "about," "for," "that," "by," "if," "and," "whether." See Understanding How Users Invoke Custom Skills to learn more about launch phrases and connecting words.
The invocation name must not contain the wake words "Alexa," "Amazon," "Echo," or the words "skill" or "app".
</li>

<li>
The invocation name must contain only lower-case alphabetic characters, spaces between words, and possessive apostrophes (for example, "sam's science trivia"). Other characters like numbers must be spelled out (for example, "twenty one"). The name must be easy to pronounce correctly and be phonetically distinct to avoid being misinterpreted as other similar sounding words.
</li>

Periods are also permissible in invocation names containing acronyms or abbreviations that are pronounced as a series of individual letters, as in “NPR”, where the letters should be all lowercase and separated by periods and spaces (for example, “n. p. r.”). However, if the abbreviation is pronounced as a word, as in “NASA”, then it should be all lowercase but not contain periods or spaces (for example, “nasa”).

The invocation name cannot spell out phonemes. For example, a skill titled "AWS Facts" would need "AWS" represented as "a. w. s. " and NOT "ay double u ess."

The invocation name must not create confusion with existing Alexa features. If your skill invocations overlap with common Alexa commands, users may get confused by Alexa's response and not enable your skill. For example, if your invocation name is too similar to the built-in "weather" command, Alexa may sometimes respond with your skill and sometimes respond with the built-in weather feature, providing an inconsistent user experience.

The invocation name must be written in each language you choose to support. For example, the German version of your skill must have an invocation name written in German. If your skill is published in a non-English marketplace, the invocation name may contain English words if these words are commonly used (for example, if proper nouns, like names and places, are used). In those cases, use the English spelling of those words. In cases where spelling differs between the local language and English, use the spelling of the local language (example: use "radioplayer" in a German skill–not "radio player").

The invocation name should be distinctive to ensure users can enable your skill. Invocation names that are too generic may be rejected during the skill certification process, or result in lower discoverability.

</ul>
