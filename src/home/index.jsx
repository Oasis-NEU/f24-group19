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
                Loading a local image:
                <br />
                <img id="wd-pants1" src="../../static/images/pants 1.jpg" height="200px" />
                <img id="wd-pants2" src="../../static/images/pants 2.jpg" height="200px" />
                <img id="wd-pants3" src="../../static/images/pants 3.jpg" height="200px" />
                <img id="wd-pants4" src="../../static/images/pants 4.jpg" height="200px" />
                <img id="wd-pants5" src="../../static/images/images%205.jpg" height="200px" />
            </div>
            <label htmlFor="top_bot"> Top/Bottom: </label><br />
            <select id="top-bot">
                <option selected value="top">Top</option>
                <option value="bottom">Bottom</option>
            </select><br />
            <label htmlFor="color"> Color: </label><br />
            <select id="color">
                <option selected value="black">Black</option>
                <option value="white">White</option>
                <option value="green">Green</option>
                <option value="navy">Navy</option>
                <option value="light blue">Light Blue</option>
                <option value="blue">Blue</option>
                <option value="beige">Beige</option>
                <option value="gray">Gray</option>
            </select><br />
            <label htmlFor="length"> Length: </label><br />
            <select id="length">
                <option selected value="shorts">Shorts</option>
                <option value="long">Long</option>
            </select><br />
            <label htmlFor="style"> Style: </label><br />
            <select id="style">
                <option selected value="sweats">Sweats</option>
                <option value="cargo">Cargo Pants</option>
                <option value="jeans">Jeans</option>
            </select></div>
        // {"clothing": "pants 1.jpg", "top_bot": "bottom", "color": "black", "length": "shorts", "style": "sweats"},
        // {"clothing": "pants 2.jpg", "top_bot": "bottom", "color": "green", "length": "long", "style": "cargo"},
        // {"clothing": "pants 3.jpg", "top_bot": "bottom", "color": "black", "length": "long", "style": "sweats"},
        // {"clothing": "pants 4.jpg", "top_bot": "bottom", "color": "white", "length": "long", "style": "sweats"},
        // {"clothing": "pants 5.jpg", "top_bot": "bottom", "color": "navy", "length": "long", "style": "jeans"},
        // {"clothing": "pants 6.jpg", "top_bot": "bottom", "color": "light blue", "length": "long", "style": "jeans"},
        // {"clothing": "pants 7.jpg", "top_bot": "bottom", "color": "black", "length": "long", "style": "jeans"},
        // {"clothing": "pants 8.jpg", "top_bot": "bottom", "color": "blue", "length": "long", "style": "slacks"},
        // {"clothing": "pants 9.jpg", "top_bot": "bottom", "color": "beige", "length": "long", "style": "slacks"},
        // {"clothing": "pants 10.jpg", "top_bot": "bottom", "color": "gray", "length": "long", "style": "slacks"}

    );
}
