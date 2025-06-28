<template>
  <nav class="cmp-headerNav">
    <ul class="cmp-headerNav__list">
      <li class="cmp-headerNav__item">
        <AtomsLink url="about">About</AtomsLink>
      </li>
      <li class="cmp-headerNav__item">
        Games
        <select class="cmp-headerNav__itemDropdown">
          <option value="game1" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="board-games">Board games</AtomsLink>
          </option>
          <option value="game2" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="card-games">Card games</AtomsLink>
          </option>
          <option value="game3" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="rpg">Role-playing games</AtomsLink>
          </option>
          <option value="game4" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="ccg">Collectible card games</AtomsLink>
          </option>
          <option value="game5" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="family-games">Family games and puzzles</AtomsLink>
          </option>
          <option value="game6" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="miniatures">Miniatures</AtomsLink>
          </option>
          <option value="game7" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="used-games">Used games</AtomsLink>
          </option>
          <option value="game8" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="game-accessories">Game accessories</AtomsLink>
          </option>
          <option value="game9" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="pre-order-plus">Pre-order Plus</AtomsLink>
          </option>
        </select>
      </li>
      <li class="cmp-headerNav__item">
        Books
        <select class="cmp-headerNav__itemDropdown">
          <option value="game1" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="comics">Comics</AtomsLink>
          </option>
          <option value="game2" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="graphic-novels">Graphic novels</AtomsLink>
          </option>
          <option value="game3" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="bundles">Bundles</AtomsLink>
          </option>
          <option value="game4" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="manga">Manga</AtomsLink>
          </option>
          <option value="game5" class="cmp-headerNav__itemDropdown-item">
            <AtomsLink url="comic-supplies">Comic supplies</AtomsLink>
          </option>
        </select>
      </li>
      <li class="cmp-headerNav__item">
        Resources
        <select class="cmp-headerNav__itemDropdown">
          <option value="game1">
            <AtomsLink url="game-rentals">Board game rentals</AtomsLink>
          </option>
          <option value="game2">
            <AtomsLink url="private-game-room-rentals"
              >Private game room rentals</AtomsLink
            >
          </option>
          <option value="game3">
            <AtomsLink url="consignment">Sell your board games</AtomsLink>
          </option>
          <option value="game4">
            <AtomsLink url="rewards">Rewards program</AtomsLink>
          </option>
          <option value="game5">
            <AtomsLink url="comic-collectors"
              >Comic collectors program</AtomsLink
            >
          </option>
          <option value="game6">
            <AtomsLink url="gob-news">GOB News</AtomsLink>
          </option>
          <option value="game7">
            <AtomsLink url="persons-of-interest"
              >GOB Persons of Interest</AtomsLink
            >
          </option>
        </select>
      </li>
      <li class="cmp-headerNav__item">
        <AtomsLink url="events">Events</AtomsLink>
      </li>
      <li class="cmp-headerNav__item">
        <AtomsLink url="login">Login</AtomsLink>
      </li>
    </ul>
  </nav>
</template>
