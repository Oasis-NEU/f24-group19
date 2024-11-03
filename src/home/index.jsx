export default function home() {
    return (
        <div>
            <header>
      <h1>Clothing Tinder</h1>
      <p>Generate clothing items that would match your style!</p>
    </header>
                <div id="wd-images">
                Select the item that you prefer:
                <br />
                <img id="wd-faker"
                    height="400px"
                    src="https://theproperlabel.us/cdn/shop/products/the-proper-tee-shirt-classic-no-logo-603222.jpg?v=1707423861"
                />
                <img id="wd-chovy"
                    height="400px"
                    src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRk7bneYFNq_nen0zwcgB6vqDWNbdbQe2zXNw&s"
                />
                <br />
                Loading a local image:
                <br />
                <img id="wd-teslabot" src="images/teslabot.jpg" height="200px" />
            </div></div>
  );}
  