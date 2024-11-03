# Local Voice

# Problem

Difficulty gathering neccessary feedback to improve city. **Examples**:

* Bus stop is damaged, someone notices, they are unsure of how to report this feedback
* Potholes in road, someone notices, they are unsure of how to report it

## Our Solution

A web app (works on mobile) where people can create pages for public places like bustops or private places such as shops , and our solution generates a qr-code that links to that page. People can scan the qr-code to access the page and can leave comments. Comments can be liked and reported. Likes are collated and are a rough measure of how important feedback is to people.

Our sytem is like a social media app but it would work close with the local authority and will be maintained by them.

If a comment is liked enough it will send an email to a pre-configured email address (to the local authority).

## Other Solutions and How we Compare

### Email

Someone could find the email of the authority responsible for maintenance. This solution is flawed as it involves a lot of effort on the part of the person reporting, as opposed to our solution which is very convient as all the user has to do is just scan the qr-code.

### Google Maps

Google Maps requires someone to create or log into a google. It also requires someone to find the place on google maps. Thousands of people visit places on google maps in real life every day, but the number of reviews left is far lower. This is evidence of the friction mentioned above stopping people from using it. Our solution has far less friction.

## Potential Issues and How we Plan to Deal with them

### Sockpuppets

A malicious user could pretend to be multiple users and mass like comments for to give them unfair influence. They could also spread spam.

We plan to combat this by using cookies on the frontend to track what posts someone have liked. This can be subverted but it means its not trivial for an attacker to mass like comments.

Comments are rate limited to reduce the impact of spam. There are two rate limits, one enforced via a token stored in a cookie on the frontend that can be subverted but prevents trival spam. A second rate limit on the server (unsubvertable) for all comments posted on a page.

Comments will be automatically removed after a set amount of time so spam attacks and malicious content will be removed eventually.

The worse outcome is that someone triggers an email to be sent, which someone could achieve already by just sending that email themselves.

### Offensive Content

Someone could use the comments to post offensive content. There is a simple text filter to catch basic offensive language. Offensive comments can reported, after a sufficient amount of reporting a comment will be removed.

The page owner can choose to enable or disable automatic removal of reported comments, they can choose to remove offensive comments themselves.

The page owner can also trigger a panic bunker, which for its duration prevents new comments being placed.

### Malicious QR Codes

A QR code obfuscated the url it leads to. A bad actor could make posters immitating the ones used by our service, and have them link to malicious sites.

Our solution to this is to have the posters mention the URL the QR code should link to. A user will be able to see if that link goes to a website in our domain. Modern smartphones allow the user to see what url they are opening when they scan a QR code, the user can then check if the url on the poster matches the one the QR code encodes.
