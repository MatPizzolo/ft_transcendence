class Player {
    #name
    #binds
    #score
    #screenSide

    constructor(name = "Player", binds = {up:"UNUSED_DEFAULT_KEY", 
    down:"UNUSED_DEFAULT_KEY", left:"UNUSED_DEFAULT_KEY", 
    right:"UNUSED_DEFAULT_KEY"}, screenSide){
        this.#name = name;
        this.#binds = binds;
        this.#score = 0;
        this.#screenSide = screenSide;
    }

    get score(){
        return this.#score;
    }
    
    get name(){
        return this.#name;
    }

    get binds(){
        return this.#binds;
    }
    
    goal(){
        this.#score += 1;
    }
    
    resetScore(){
        this.#score = 0;
    }

}   