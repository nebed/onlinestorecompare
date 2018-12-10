
Vue.component('price-slide' , {
  template: `<div>
  <vue-slider :value="value" v-on:input="$emit('input', $event)" v-bind="options">
  </vue-slider>  
</div>`,
  props: {
    iniValue: Array,
    value: { type: [Array, Number, String] }
  },
  data: function data() {
    return {
      // tooltip : '',
      // value: [40,60],
      options: {
        eventType: 'auto',
        width: 'auto',
        height: 8,
        dotSize: 20,
        min: this.iniValue[0],
        max: this.iniValue[1],
        interval: 1,
        show: true,
        speed: 0.5,
        disabled: false,
        piecewise: false,
        piecewiseStyle: false,
        piecewiseLabel: false,
        tooltip: "always", // why was this false, you want a tooltip, don't you? Yes i want, but didn't dig in plug setting such a dip untill now.
        tooltipDir: ['left','right'],
        reverse: false,
        data: null,
        clickable: true,
        realTime: false,
        lazy: false,
        formatter: null,
        bgStyle:  {
  "backgroundColor": "#fff",
  "boxShadow": "inset 0.5px 0.5px 3px 1px rgba(0,0,0,.36)"
},
        sliderStyle: [
  {
    "backgroundColor": "#f7b733"
  },
  {
    "backgroundColor": "#4abdac"
  }
],
        processStyle: {
  "backgroundImage": "-webkit-linear-gradient(left, #f7b733, #4abdac)"
},
        piecewiseActiveStyle: null,
        piecewiseStyle: null,
        tooltipStyle: [
  {
    "backgroundColor": "#f7b733",
    "borderColor": "#f7b733"
  },
  {
    "backgroundColor": "#4abdac",
    "borderColor": "#4abdac"
  }
],
        labelStyle: null,
        labelActiveStyle: null
      }
    };
  },

  components: {
    'vueSlider': window['vue-slider-component']
  },
  watch: {
      value: function (){
         
      }
  }
});


Vue.component('search-result', {

	props: ['store','image','url','title','price'],

	template: `
			<div class="slideout-item scaleup" v-touch:swipe.right="onSwipeLeft">
            <div :class="store" class="card card-border-color">
                <div class="card-body">
                  <div class="row">
                  <div class="col-md-5 col-5 col-sm-5 col-xs-5">
                    <div class="align-middle mtb-auto"><a :href="url"><img class="img-fluid" :src="image" style="width:120px;"></a></div>
                  </div>
                  <div class="col-md-7 col-7 col-sm-7 col-xs-7">
                    <a :href="url" class="cl1"><p><strong v-text=title></strong></p></a>
                    <p>₦{{ price }}</p>
                    <button @click="showProduct" data-toggle="modal" data-target="#myModal" :class="'bg-'+ store" class="btn btn-primary btn-block"> Buy from {{ store }}</button>
                  </div>
                </div>
                </div>
              </div>
          	</div>
    `,
    methods: {
    
            showProduct() {
              this.$emit('clicked', {'url':this.url, 'store':this.store});
            },
            onSwipeLeft() {
              this.$emit('removed');
            }
    }
});

Vue.component('lazy-load', {

	props: [],

	template: `
			<div class="col-lg-4 col-md-4 mb-3">
            <div class="lazy-div">
                  <div class="row">
                  <div class="col-md-5 col-5 col-sm-5 col-xs-5 animated-background">
                    
                  </div>
                  <div class="col-md-7 col-7 col-sm-7 col-xs-7">
                    <div class="animated-text lazy-text"></div>
                    <div class="animated-text lazy-text"></div>
                    <div class="animated-text lazy-text"></div>
                    <div class="animated-text lazy-text"></div>
                  </div>
                </div>
              </div>
            </div>
    `

});


var app = new Vue({

			el: '#root',
			data: {

				term : "",
        filterbyname: "",
				results: [],
				loading: false,
        productUrl: "",
        checkedStores: [],
        itemBeforeAds: 10,
        height: { value: [0,700000], min: 0, max: 700000 },
				
			},

			computed: {
				searchResults() {
          if (this.checkedStores.length == 0 ){
             var products = this.results.sort((a,b)=>parseFloat(a.price) - parseFloat(b.price));
          } else {
           var products = this.results.sort((a,b)=>parseFloat(a.price) - parseFloat(b.price)).filter((product) => {
              return this.checkedStores.includes(product.source.toLowerCase());
            });
          }
          var priceranges = products.filter((product) => { return parseFloat(product.price) >= this.height.value[0] && parseFloat(product.price) <= this.height.value[1];});
          return priceranges.filter((pricerange) => {
            if (isNaN(this.filterbyname) || this.filterbyname == "" || this.filterbyname == null){
              return pricerange.title.toLowerCase().includes(this.filterbyname.toLowerCase());
            }
          });
				},
        rowCount: function(){     
        return Math.ceil(this.searchResults.length / this.itemsBeforeAds);
      },
				
			},

			methods : {

				getResults() {
					this.loading = true;
					axios.get('/search/' + this.term).then(response => {this.loading = false; return this.results = response.data;}).catch(error => { this.loading = false; return console.log(error);});
				},

        setUrl(args) {
                this.productUrl = 'https://onlinestorecompare.herokuapp.com/product?url=' + args.url + '&store=' + args.store;
            },
        deleteElement(index) {
                this.results.splice(index, 1);;
            }
			},
      watch: {
      height: function (){
          console.log(this.height.value)
      }
  }

		});