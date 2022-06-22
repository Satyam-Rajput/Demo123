$(document).ready(function() {
    var $country = $('#country');
    var $state = $('#state');
    var $city = $('#city');
    $country.val('Country');



    $country.change(function(e) {
        e.preventDefault();

        $city.empty();
        $state.empty();


        switch ($country.val()) {
            case 'India':
                $city.html(`<option class="text-dark" selected>City</option>`);
                $state.html(`<option class="text-dark" selected>State</option>
                
                <option value="Madhya Pradesh">Madhya Pradesh</option>
                <option value="Uttar Pradesh">Uttar Pradesh</option>
                <option value="Delhi">Delhi</option>
                <option value="Bihar">Bihar</option>
                <option value="Uttarakhand">Uttarakhand</option>
                
                `);

                break;

            case 'Nepal':
                $city.html(`<option class="text-dark" selected>City</option>`);
                $state.html(`<option class="text-dark" selected>State</option>
                    <option value="Kathmandu">Kathmandu</option>
                    <option value="Pokhara">Pokhara</option>
                    <option value="Lalitpur">Lalitpur</option>
                    
                    <option value="Bharatpur">Bharatpur</option>
                   
                    
                    `);

                break;

            case 'Sri Lanka':
                $city.html(`<option class="text-dark" selected>City</option>`);
                $state.html(`<option class="text-dark" selected>State</option>
                    <option value="Anuradhapura">Anuradhapura</option>
                    <option value="Colombo">Colombo</option>
                    <option value="Puttalam">Puttalam</option>
                    
                    <option value="Trincomalee">Trincomalee</option>
                   
                    
                    `);

                break;

            default:
                $state.html(`<option class="text-dark" selected>State</option>`);
                $city.html(`<option class="text-dark" selected>City</option>`);
        }




    });








    $state.change(function(e) {
        e.preventDefault();

        $city.empty();
        $city.html(`<option class="text-dark" selected>City</option>`);


        switch ($state.val()) {
            case 'Uttar Pradesh':
                $city.html(`<option class="text-dark" selected>City</option>
                <option value="Kanpur">Kanpur</option>
                <option value="Etawah">Etawah</option>
                <option value="Agra">Agra</option>
                
                <option value="Lucknow">Lucknow</option>
                <option value="Noida">Noida</option>
                
                `);

                break;

            case 'Kathmandu':
                $city.html(`<option class="text-dark" selected>City</option>
                    <option value="Kathmandu">Kathmandu</option>
                    <option value="Pokhara">Pokhara</option>
                    <option value="Lalitpur">Lalitpur</option>
                    
                    <option value="Bharatpur">Bharatpur</option>
                   
                    
                    `);

                break;

            case 'Anuradhapura':
                $city.html(`<option class="text-dark" selected>City</option>
                    <option value="Anuradhapura">Anuradhapura</option>
                    <option value="Colombo">Colombo</option>
                    <option value="Puttalam">Puttalam</option>
                    
                    <option value="Trincomalee">Trincomalee</option>
                   
                    
                    `);

                break;

            default:
                // $state.html(`<option class="text-dark" selected>State</option>`);
                $city.html(`<option class="text-dark" selected>City</option>`);
        }




    });


});