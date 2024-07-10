# party-css
I love party parrots. My boss regrettably does not. I made this to try to convert him over to liking them, by partifying the frontend of the product I work on (it didn't work, somehow he hates party parrots even more).

On a basal level, this repo has a `🦜` css class which will make whatever html element its applied to 'partified'. It makes HTML elements bob in an oval and change rainbow colours. Neat!

The implementation is very simple. It's fundamentally just two animations, a `party` and a `tint`.

```css
.🦜 {
  animation: party 0.7s infinite, tint 0.7s infinite;
  transform-origin: bottom center;
}
```

The `tint` animation is responsible for the colour. It was created by manually sampling the [party parrot gif](https://cultofthepartyparrot.com/) at nine eqispaced points. 

`party` on the other hand is responsible for the motion. It is created by `party_skew_gen.py`, which calculates X skew and Y scale components to make a seamless, partyparrot esque monstrosity.

It's not perfect. It could be faster, the X skew could be larger. If you want to improve on this feel free - it's merely parameter turning with the code generation and modifying the animation times.

![parrot](https://cultofthepartyparrot.com/parrots/hd/parrot.gif)

# Party or die!
