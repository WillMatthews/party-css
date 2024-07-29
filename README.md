# party-css
I love party parrots. My boss regrettably does not. I made this to try to convert him over to liking them, by partifying the frontend of the product I work on (it didn't work, somehow he hates party parrots even more).

On a basal level, this repo has a `🦜` css class which will make whatever html element its applied to 'partified'. It makes HTML elements bob in an oval and change rainbow colours. Neat!

The implementation is very simple. It's fundamentally just two animations, a `🎉` and a `🎨`.

```css
.🦜 {
  animation: 🎉 0.7s infinite linear, 🎨 0.7s infinite linear;
  transform-origin: bottom center;
}
```

The `🎨` animation is responsible for the colour. It was created by manually sampling the [party parrot gif](https://cultofthepartyparrot.com/) at nine eqispaced points. 

`🎉` on the other hand is responsible for the motion. It is created by `party_skew_gen.py`, which calculates X skew and Y scale components to make a seamless, partyparrot esque monstrosity.

It's not perfect. It could be faster, the X skew could be larger. If you want to improve on this feel free - it's merely parameter turning with the code generation and modifying the animation times.

![parrot](https://cultofthepartyparrot.com/parrots/hd/parrot.gif)

[see it in action on jsfiddle](https://jsfiddle.net/pg926wh1/1/)

![in-action](/doc/party-demo.webp)

# Party or die!
